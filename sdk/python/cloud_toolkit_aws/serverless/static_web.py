# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ..bucket import _storage.Bucket
from ._inputs import *
import pulumi_aws

__all__ = ['StaticWebArgs', 'StaticWeb']

@pulumi.input_type
class StaticWebArgs:
    def __init__(__self__, *,
                 cache: Optional[pulumi.Input['CdnCacheArgsArgs']] = None,
                 configure_dns: Optional[pulumi.Input[bool]] = None,
                 dns: Optional[pulumi.Input['CdnDnsArgsArgs']] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 include_www: Optional[pulumi.Input[bool]] = None,
                 price_class: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StaticWeb resource.
        :param pulumi.Input['CdnCacheArgsArgs'] cache: Cloud Front distribution cache
        :param pulumi.Input[bool] configure_dns: Set to true to configure DNS
        :param pulumi.Input['CdnDnsArgsArgs'] dns: DNS configuration
        :param pulumi.Input[str] domain: Set to true to add an alias to wwww.<domain>
        :param pulumi.Input[bool] include_www: Set to true to add an alias to wwww.<domain>
        :param pulumi.Input[str] price_class: Cloud Front distribution priceClass
        """
        if cache is not None:
            pulumi.set(__self__, "cache", cache)
        if configure_dns is not None:
            pulumi.set(__self__, "configure_dns", configure_dns)
        if dns is not None:
            pulumi.set(__self__, "dns", dns)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if include_www is not None:
            pulumi.set(__self__, "include_www", include_www)
        if price_class is not None:
            pulumi.set(__self__, "price_class", price_class)

    @property
    @pulumi.getter
    def cache(self) -> Optional[pulumi.Input['CdnCacheArgsArgs']]:
        """
        Cloud Front distribution cache
        """
        return pulumi.get(self, "cache")

    @cache.setter
    def cache(self, value: Optional[pulumi.Input['CdnCacheArgsArgs']]):
        pulumi.set(self, "cache", value)

    @property
    @pulumi.getter(name="configureDNS")
    def configure_dns(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true to configure DNS
        """
        return pulumi.get(self, "configure_dns")

    @configure_dns.setter
    def configure_dns(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "configure_dns", value)

    @property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input['CdnDnsArgsArgs']]:
        """
        DNS configuration
        """
        return pulumi.get(self, "dns")

    @dns.setter
    def dns(self, value: Optional[pulumi.Input['CdnDnsArgsArgs']]):
        pulumi.set(self, "dns", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Set to true to add an alias to wwww.<domain>
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="includeWWW")
    def include_www(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true to add an alias to wwww.<domain>
        """
        return pulumi.get(self, "include_www")

    @include_www.setter
    def include_www(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_www", value)

    @property
    @pulumi.getter(name="priceClass")
    def price_class(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud Front distribution priceClass
        """
        return pulumi.get(self, "price_class")

    @price_class.setter
    def price_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "price_class", value)


class StaticWeb(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache: Optional[pulumi.Input[pulumi.InputType['CdnCacheArgsArgs']]] = None,
                 configure_dns: Optional[pulumi.Input[bool]] = None,
                 dns: Optional[pulumi.Input[pulumi.InputType['CdnDnsArgsArgs']]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 include_www: Optional[pulumi.Input[bool]] = None,
                 price_class: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a StaticWeb resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CdnCacheArgsArgs']] cache: Cloud Front distribution cache
        :param pulumi.Input[bool] configure_dns: Set to true to configure DNS
        :param pulumi.Input[pulumi.InputType['CdnDnsArgsArgs']] dns: DNS configuration
        :param pulumi.Input[str] domain: Set to true to add an alias to wwww.<domain>
        :param pulumi.Input[bool] include_www: Set to true to add an alias to wwww.<domain>
        :param pulumi.Input[str] price_class: Cloud Front distribution priceClass
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StaticWebArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a StaticWeb resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param StaticWebArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticWebArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache: Optional[pulumi.Input[pulumi.InputType['CdnCacheArgsArgs']]] = None,
                 configure_dns: Optional[pulumi.Input[bool]] = None,
                 dns: Optional[pulumi.Input[pulumi.InputType['CdnDnsArgsArgs']]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 include_www: Optional[pulumi.Input[bool]] = None,
                 price_class: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StaticWebArgs.__new__(StaticWebArgs)

            __props__.__dict__["cache"] = cache
            __props__.__dict__["configure_dns"] = configure_dns
            __props__.__dict__["dns"] = dns
            __props__.__dict__["domain"] = domain
            __props__.__dict__["include_www"] = include_www
            __props__.__dict__["price_class"] = price_class
            __props__.__dict__["dns_records"] = None
            __props__.__dict__["dns_records_for_validation"] = None
            __props__.__dict__["certificate"] = None
            __props__.__dict__["certificate_validation"] = None
            __props__.__dict__["content_bucket"] = None
            __props__.__dict__["content_bucket_policy"] = None
            __props__.__dict__["distribution"] = None
            __props__.__dict__["domain_validation_options"] = None
            __props__.__dict__["east_region"] = None
            __props__.__dict__["logs_bucket"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["origin_access_identity"] = None
        super(StaticWeb, __self__).__init__(
            'cloud-toolkit-aws:serverless:StaticWeb',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="DNSRecords")
    def dns_records(self) -> pulumi.Output[Optional['outputs.DNSRecordsArgs']]:
        """
        DNS Records to expose staticweb
        """
        return pulumi.get(self, "dns_records")

    @property
    @pulumi.getter(name="DNSRecordsForValidation")
    def dns_records_for_validation(self) -> pulumi.Output[Optional['outputs.DNSRecordsArgs']]:
        """
        DNS Records to validate the certificate
        """
        return pulumi.get(self, "dns_records_for_validation")

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[Optional['pulumi_aws.acm.Certificate']]:
        """
        CloudFront Distribution
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="certificateValidation")
    def certificate_validation(self) -> pulumi.Output[Optional['pulumi_aws.acm.CertificateValidation']]:
        """
        AWS certificate validation
        """
        return pulumi.get(self, "certificate_validation")

    @property
    @pulumi.getter(name="contentBucket")
    def content_bucket(self) -> pulumi.Output['_storage.Bucket']:
        """
        Content bucket
        """
        return pulumi.get(self, "content_bucket")

    @property
    @pulumi.getter(name="contentBucketPolicy")
    def content_bucket_policy(self) -> pulumi.Output['pulumi_aws.s3.BucketPolicy']:
        """
        Bucket policy to connect Cloud Front distribution
        """
        return pulumi.get(self, "content_bucket_policy")

    @property
    @pulumi.getter
    def distribution(self) -> pulumi.Output['pulumi_aws.cloudfront.Distribution']:
        """
        CloudFront Distribution
        """
        return pulumi.get(self, "distribution")

    @property
    @pulumi.getter(name="domainValidationOptions")
    def domain_validation_options(self) -> pulumi.Output[Optional[Sequence['pulumi_aws.acm.outputs.CertificateDomainValidationOption']]]:
        """
        CloudFront Distribution
        """
        return pulumi.get(self, "domain_validation_options")

    @property
    @pulumi.getter(name="eastRegion")
    def east_region(self) -> pulumi.Output['pulumi_aws.Provider']:
        """
        AWS eastRegion provider. It is required to create and validate certificates
        """
        return pulumi.get(self, "east_region")

    @property
    @pulumi.getter(name="logsBucket")
    def logs_bucket(self) -> pulumi.Output['pulumi_aws.s3.Bucket']:
        """
        Logs bucket
        """
        return pulumi.get(self, "logs_bucket")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Staticweb name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originAccessIdentity")
    def origin_access_identity(self) -> pulumi.Output['pulumi_aws.cloudfront.OriginAccessIdentity']:
        """
        OriginAccessIdentity to have access to content bucket
        """
        return pulumi.get(self, "origin_access_identity")

