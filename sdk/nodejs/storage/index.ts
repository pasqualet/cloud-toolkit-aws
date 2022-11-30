// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { BucketArgs } from "./bucket";
export type Bucket = import("./bucket").Bucket;
export const Bucket: typeof import("./bucket").Bucket = null as any;
utilities.lazyLoad(exports, ["Bucket"], () => require("./bucket"));


// Export enums:
export * from "../types/enums/storage";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "cloud-toolkit-aws:storage:Bucket":
                return new Bucket(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("cloud-toolkit-aws", "storage", _module)
