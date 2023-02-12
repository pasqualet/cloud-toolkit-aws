VERSION         := $(shell pulumictl get version)

PACK            := cloud-toolkit-aws
PROJECT         := github.com/cloud-toolkit/${PACK}

PROVIDER        := pulumi-resource-${PACK}
CODEGEN         := pulumi-gen-${PACK}

WORKING_DIR     := $(shell pwd)
SCHEMA_PATH     := ${WORKING_DIR}/schema.yaml

generate:: gen_go_sdk gen_nodejs_sdk gen_python_sdk

build_sdk:: build_nodejs_sdk build_python_sdk

build:: build_provider 

install:: install_provider

build_provider::
	cd provider/cmd/${PROVIDER}/ && \
		npm ci && \
		npx tsc && \
		cp package.json ../../../schema.yaml ./bin && \
		sed -i.back -e "s/\$${VERSION}/$(VERSION)/g" bin/package.json

install_provider:: PKG_ARGS := --no-bytecode --public-packages "*" --public
install_provider:: build_provider
	rm -rf bin && \
	    cd provider/cmd/${PROVIDER}/ && \
        npx pkg . ${PKG_ARGS} --target node16 --output ../../../bin/${PROVIDER}

gen_go_sdk::
	rm -rf sdk/go
	cd provider/cmd/${CODEGEN} && go run . go ../../../sdk/go ${SCHEMA_PATH}

gen_nodejs_sdk::
	rm -rf sdk/nodejs
	cd provider/cmd/${CODEGEN} && go run . nodejs ../../../sdk/nodejs ${SCHEMA_PATH}
	echo 'import "@pulumi/aws";' >> sdk/nodejs/index.ts
	echo 'import "@pulumi/kubernetes";' >> sdk/nodejs/index.ts
	echo 'import "@pulumi/random";' >> sdk/nodejs/index.ts

build_nodejs_sdk:: VERSION := $(shell pulumictl get version --language javascript)
build_nodejs_sdk:: gen_nodejs_sdk
	cd sdk/nodejs/ && \
		echo "module fake_nodejs_module // Exclude this directory from Go tools\n\ngo 1.18" > go.mod && \
		npm install && \
		npm run build && \
		cp -R scripts bin/ && \
		cp ../../README.md ../../LICENSE package.json package-lock.json ./bin/ && \
		sed -i.bak -e "s/\$${VERSION}/$(VERSION)/g" ./bin/package.json && \
		rm ./bin/package.json.bak

release_nodejs_sdk::
	cd sdk/nodejs/bin && \
		npm publish

gen_python_sdk::
	rm -rf sdk/python
	cd provider/cmd/${CODEGEN} && go run . python ../../../sdk/python ${SCHEMA_PATH}
	cp ${WORKING_DIR}/README.md sdk/python

build_python_sdk:: PYPI_VERSION := $(shell pulumictl get version --language python)
build_python_sdk:: gen_python_sdk
	cd sdk/python/ && \
		echo "module fake_python_module // Exclude this directory from Go tools\n\ngo 1.18" > go.mod && \
		cp ../../README.md . && \
		python3 setup.py clean --all 2>/dev/null && \
		rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
		sed -i.bak -e 's/^VERSION = .*/VERSION = "$(PYPI_VERSION)"/g' -e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(VERSION)"/g' ./bin/setup.py && \
		rm ./bin/setup.py.bak && \
		cd ./bin && python3 setup.py build sdist

release_python_sdk::
	cd sdk/python/bin && \
		pip3 install twine && \
		twine upload dist/*

dist:: PKG_ARGS := --no-bytecode --public-packages "*" --public
dist:: build_provider
	cd provider/cmd/${PROVIDER}/ && \
		npx pkg . ${PKG_ARGS} --target node16-macos-x64 --output ../../../bin/darwin-amd64/${PROVIDER} && \
		npx pkg . ${PKG_ARGS} --target node16-macos-arm64 --output ../../../bin/darwin-arm64/${PROVIDER} && \
		npx pkg . ${PKG_ARGS} --target node16-linuxstatic-x64 --output ../../../bin/linux-amd64/${PROVIDER} && \
		npx pkg . ${PKG_ARGS} --target node16-linuxstatic-arm64 --output ../../../bin/linux-arm64/${PROVIDER} && \
		npx pkg . ${PKG_ARGS} --target node16-win-x64 --output ../../../bin/windows-amd64/${PROVIDER}.exe
	mkdir -p dist
	tar --gzip -cf ./dist/pulumi-resource-${PACK}-v${VERSION}-linux-amd64.tar.gz README.md LICENSE -C bin/linux-amd64/ .
	tar --gzip -cf ./dist/pulumi-resource-${PACK}-v${VERSION}-linux-arm64.tar.gz README.md LICENSE -C bin/linux-arm64/ .
	tar --gzip -cf ./dist/pulumi-resource-${PACK}-v${VERSION}-darwin-amd64.tar.gz README.md LICENSE -C bin/darwin-amd64/ .
	tar --gzip -cf ./dist/pulumi-resource-${PACK}-v${VERSION}-darwin-arm64.tar.gz README.md LICENSE -C bin/darwin-arm64/ .
	tar --gzip -cf ./dist/pulumi-resource-${PACK}-v${VERSION}-windows-amd64.tar.gz README.md LICENSE -C bin/windows-amd64/ .

version::
	@echo ${VERSION}

integration_tests_storage::
		ginkgo run --junit-report report.xml --json-report report.json -r --keep-going --output-dir tests-result -race -trace -cover ./tests/suites/storage

integration_tests_kubernetes::
		ginkgo run --junit-report report.xml --json-report report.json -r --keep-going --output-dir tests-result -race -trace -cover ./tests/suites/kubernetes

integration_tests_serverless::
		ginkgo run --junit-report report.xml --json-report report.json -r --keep-going --output-dir tests-result -race -trace -cover ./tests/suites/serverless

integration_tests_databases::
		ginkgo run --junit-report report.xml --json-report report.json -r --keep-going --output-dir tests-result -race -trace -cover ./tests/suites/databases

prepare_integration_tests::
	rm -rf ~/.config/yarn/link/@cloudtoolkit/aws && \
		(cd sdk/nodejs/bin && yarn link) && \
		(cd tests && go mod download) && \
		go install github.com/onsi/ginkgo/v2/ginkgo@v2.6.1

integration_tests:: prepare_integration_tests
		ginkgo run -vv --junit-report report.xml --json-report report.json -r --keep-going --output-dir tests-result -race -trace -cover ./tests
