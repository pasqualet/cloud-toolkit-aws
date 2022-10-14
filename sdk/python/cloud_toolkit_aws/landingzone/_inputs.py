# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'AccountIamArgsArgs',
    'AccountPasswordPolicyArgsArgs',
    'AccountPasswordPolicyRulesArgsArgs',
    'AuditLoggingCloudWatchArgsArgs',
    'IamTrustedAccountRoleArgsArgs',
    'IamTrustingAccountRoleArgsArgs',
    'LandingZoneAuditArgsArgs',
    'LandingZoneAuditCloudWatchArgsArgs',
    'LandingZoneIamArgsArgs',
    'LandingZoneIamRoleArgsArgs',
    'OrganizationAccountArgsArgs',
    'OrganizationArgsArgs',
    'OrganizationPoliciesArgsArgs',
    'OrganizationPolicyArgsArgs',
]

@pulumi.input_type
class AccountIamArgsArgs:
    def __init__(__self__, *,
                 alias: Optional[pulumi.Input[str]] = None,
                 password_policy: Optional[pulumi.Input['AccountPasswordPolicyArgsArgs']] = None):
        """
        :param pulumi.Input[str] alias: The alias to be used for IAM.
        :param pulumi.Input['AccountPasswordPolicyArgsArgs'] password_policy: The IAM password policy configuration.
        """
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if password_policy is not None:
            pulumi.set(__self__, "password_policy", password_policy)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias to be used for IAM.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter(name="passwordPolicy")
    def password_policy(self) -> Optional[pulumi.Input['AccountPasswordPolicyArgsArgs']]:
        """
        The IAM password policy configuration.
        """
        return pulumi.get(self, "password_policy")

    @password_policy.setter
    def password_policy(self, value: Optional[pulumi.Input['AccountPasswordPolicyArgsArgs']]):
        pulumi.set(self, "password_policy", value)


@pulumi.input_type
class AccountPasswordPolicyArgsArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 rules: Optional[pulumi.Input['AccountPasswordPolicyRulesArgsArgs']] = None):
        """
        :param pulumi.Input[bool] enabled: Enable the creation of IAM Password Policy. Defaults to 'true'.
        :param pulumi.Input['AccountPasswordPolicyRulesArgsArgs'] rules: The rules to be applied to the IAM Password Policy
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable the creation of IAM Password Policy. Defaults to 'true'.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input['AccountPasswordPolicyRulesArgsArgs']]:
        """
        The rules to be applied to the IAM Password Policy
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input['AccountPasswordPolicyRulesArgsArgs']]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class AccountPasswordPolicyRulesArgsArgs:
    def __init__(__self__, *,
                 allow_users_to_change_password: Optional[pulumi.Input[bool]] = None,
                 hard_expiry: Optional[pulumi.Input[bool]] = None,
                 max_password_age: Optional[pulumi.Input[float]] = None,
                 minimum_password_length: Optional[pulumi.Input[float]] = None,
                 password_reuse_prevention: Optional[pulumi.Input[float]] = None,
                 require_lowercase_characters: Optional[pulumi.Input[bool]] = None,
                 require_numbers: Optional[pulumi.Input[bool]] = None,
                 require_symbols: Optional[pulumi.Input[bool]] = None,
                 require_uppercase_characters: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] allow_users_to_change_password: Whether to allow users to change their own password. Defaults to 'true'.
        :param pulumi.Input[bool] hard_expiry: Whether users are prevented from setting a new password after their password has expired (i.e., require administrator reset). Defaults to 'true'.
        :param pulumi.Input[float] max_password_age: The number of days that an user password is valid. Defaults to '90'.
        :param pulumi.Input[float] minimum_password_length: Minimum length to require for user passwords. Defaults to '14'.
        :param pulumi.Input[float] password_reuse_prevention: The number of previous passwords that users are prevented from reusing. Defaults to '0'.
        :param pulumi.Input[bool] require_lowercase_characters: Whether to require lowercase characters for user passwords. Defaults to 'true'.
        :param pulumi.Input[bool] require_numbers: Whether to require numbers for user passwords. Defaults to 'true'.
        :param pulumi.Input[bool] require_symbols: Whether to require symbols for user passwords. Defaults to 'true'.
        :param pulumi.Input[bool] require_uppercase_characters: Whether to require uppercase characters for user passwords. Defaults to 'true'.
        """
        if allow_users_to_change_password is not None:
            pulumi.set(__self__, "allow_users_to_change_password", allow_users_to_change_password)
        if hard_expiry is not None:
            pulumi.set(__self__, "hard_expiry", hard_expiry)
        if max_password_age is not None:
            pulumi.set(__self__, "max_password_age", max_password_age)
        if minimum_password_length is not None:
            pulumi.set(__self__, "minimum_password_length", minimum_password_length)
        if password_reuse_prevention is not None:
            pulumi.set(__self__, "password_reuse_prevention", password_reuse_prevention)
        if require_lowercase_characters is not None:
            pulumi.set(__self__, "require_lowercase_characters", require_lowercase_characters)
        if require_numbers is not None:
            pulumi.set(__self__, "require_numbers", require_numbers)
        if require_symbols is not None:
            pulumi.set(__self__, "require_symbols", require_symbols)
        if require_uppercase_characters is not None:
            pulumi.set(__self__, "require_uppercase_characters", require_uppercase_characters)

    @property
    @pulumi.getter(name="allowUsersToChangePassword")
    def allow_users_to_change_password(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to allow users to change their own password. Defaults to 'true'.
        """
        return pulumi.get(self, "allow_users_to_change_password")

    @allow_users_to_change_password.setter
    def allow_users_to_change_password(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_users_to_change_password", value)

    @property
    @pulumi.getter(name="hardExpiry")
    def hard_expiry(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether users are prevented from setting a new password after their password has expired (i.e., require administrator reset). Defaults to 'true'.
        """
        return pulumi.get(self, "hard_expiry")

    @hard_expiry.setter
    def hard_expiry(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hard_expiry", value)

    @property
    @pulumi.getter(name="maxPasswordAge")
    def max_password_age(self) -> Optional[pulumi.Input[float]]:
        """
        The number of days that an user password is valid. Defaults to '90'.
        """
        return pulumi.get(self, "max_password_age")

    @max_password_age.setter
    def max_password_age(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_password_age", value)

    @property
    @pulumi.getter(name="minimumPasswordLength")
    def minimum_password_length(self) -> Optional[pulumi.Input[float]]:
        """
        Minimum length to require for user passwords. Defaults to '14'.
        """
        return pulumi.get(self, "minimum_password_length")

    @minimum_password_length.setter
    def minimum_password_length(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "minimum_password_length", value)

    @property
    @pulumi.getter(name="passwordReusePrevention")
    def password_reuse_prevention(self) -> Optional[pulumi.Input[float]]:
        """
        The number of previous passwords that users are prevented from reusing. Defaults to '0'.
        """
        return pulumi.get(self, "password_reuse_prevention")

    @password_reuse_prevention.setter
    def password_reuse_prevention(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "password_reuse_prevention", value)

    @property
    @pulumi.getter(name="requireLowercaseCharacters")
    def require_lowercase_characters(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to require lowercase characters for user passwords. Defaults to 'true'.
        """
        return pulumi.get(self, "require_lowercase_characters")

    @require_lowercase_characters.setter
    def require_lowercase_characters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_lowercase_characters", value)

    @property
    @pulumi.getter(name="requireNumbers")
    def require_numbers(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to require numbers for user passwords. Defaults to 'true'.
        """
        return pulumi.get(self, "require_numbers")

    @require_numbers.setter
    def require_numbers(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_numbers", value)

    @property
    @pulumi.getter(name="requireSymbols")
    def require_symbols(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to require symbols for user passwords. Defaults to 'true'.
        """
        return pulumi.get(self, "require_symbols")

    @require_symbols.setter
    def require_symbols(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_symbols", value)

    @property
    @pulumi.getter(name="requireUppercaseCharacters")
    def require_uppercase_characters(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to require uppercase characters for user passwords. Defaults to 'true'.
        """
        return pulumi.get(self, "require_uppercase_characters")

    @require_uppercase_characters.setter
    def require_uppercase_characters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_uppercase_characters", value)


@pulumi.input_type
class AuditLoggingCloudWatchArgsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 retention_days: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[bool] enabled: Enable storing audit logs in CloudWatch. Defaults to 'false'.
        :param pulumi.Input[float] retention_days: The data retention in days. Defaults to '1'.
        """
        pulumi.set(__self__, "enabled", enabled)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Enable storing audit logs in CloudWatch. Defaults to 'false'.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[float]]:
        """
        The data retention in days. Defaults to '1'.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "retention_days", value)


@pulumi.input_type
class IamTrustedAccountRoleArgsArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class IamTrustingAccountRoleArgsArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 policy_names: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "policy_names", policy_names)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "policy_names")

    @policy_names.setter
    def policy_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "policy_names", value)


@pulumi.input_type
class LandingZoneAuditArgsArgs:
    def __init__(__self__, *,
                 account_name: Optional[pulumi.Input[str]] = None,
                 cloudwatch: Optional[pulumi.Input['LandingZoneAuditCloudWatchArgsArgs']] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 retention_days: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] account_name: Select the Organization account to be used to store the audit logs.
        :param pulumi.Input['LandingZoneAuditCloudWatchArgsArgs'] cloudwatch: Store the audit logs in CloudWatch to enable easy searching.
        :param pulumi.Input[bool] enabled: Enable audit logging. Defaults to 'true'.
        :param pulumi.Input[float] retention_days: The data retention in days. Defaults to '7'.
        """
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if cloudwatch is not None:
            pulumi.set(__self__, "cloudwatch", cloudwatch)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Select the Organization account to be used to store the audit logs.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def cloudwatch(self) -> Optional[pulumi.Input['LandingZoneAuditCloudWatchArgsArgs']]:
        """
        Store the audit logs in CloudWatch to enable easy searching.
        """
        return pulumi.get(self, "cloudwatch")

    @cloudwatch.setter
    def cloudwatch(self, value: Optional[pulumi.Input['LandingZoneAuditCloudWatchArgsArgs']]):
        pulumi.set(self, "cloudwatch", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable audit logging. Defaults to 'true'.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[float]]:
        """
        The data retention in days. Defaults to '7'.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "retention_days", value)


@pulumi.input_type
class LandingZoneAuditCloudWatchArgsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 retention_days: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[bool] enabled: Enable storing audit logs in CloudWatch. Defaults to 'false'.
        :param pulumi.Input[float] retention_days: The data retention in days. Defaults to '1'.
        """
        pulumi.set(__self__, "enabled", enabled)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Enable storing audit logs in CloudWatch. Defaults to 'false'.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[float]]:
        """
        The data retention in days. Defaults to '1'.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "retention_days", value)


@pulumi.input_type
class LandingZoneIamArgsArgs:
    def __init__(__self__, *,
                 account_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input['LandingZoneIamRoleArgsArgs']]]] = None):
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LandingZoneIamRoleArgsArgs']]]]:
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LandingZoneIamRoleArgsArgs']]]]):
        pulumi.set(self, "roles", value)


@pulumi.input_type
class LandingZoneIamRoleArgsArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 policy_names: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "policy_names", policy_names)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "policy_names")

    @policy_names.setter
    def policy_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "policy_names", value)


@pulumi.input_type
class OrganizationAccountArgsArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 iam: pulumi.Input['AccountIamArgsArgs'],
                 name: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 admin_role_name: Optional[pulumi.Input[str]] = None,
                 ou: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] email: The email associated to the IAM Account.
        :param pulumi.Input['AccountIamArgsArgs'] iam: The configuration for IAM.
        :param pulumi.Input[str] name: The name of the IAM Account.
        :param pulumi.Input[str] account_id: The AWS Account ID to be used to import the Account in the Organization. If not set, a new AWS Account will be created.
        :param pulumi.Input[str] admin_role_name: Admin role for the IAM Account.
        :param pulumi.Input[str] parent_id: The parentId of the imported account.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "iam", iam)
        pulumi.set(__self__, "name", name)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if admin_role_name is not None:
            pulumi.set(__self__, "admin_role_name", admin_role_name)
        if ou is not None:
            pulumi.set(__self__, "ou", ou)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        The email associated to the IAM Account.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def iam(self) -> pulumi.Input['AccountIamArgsArgs']:
        """
        The configuration for IAM.
        """
        return pulumi.get(self, "iam")

    @iam.setter
    def iam(self, value: pulumi.Input['AccountIamArgsArgs']):
        pulumi.set(self, "iam", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the IAM Account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Account ID to be used to import the Account in the Organization. If not set, a new AWS Account will be created.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="adminRoleName")
    def admin_role_name(self) -> Optional[pulumi.Input[str]]:
        """
        Admin role for the IAM Account.
        """
        return pulumi.get(self, "admin_role_name")

    @admin_role_name.setter
    def admin_role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_role_name", value)

    @property
    @pulumi.getter
    def ou(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ou")

    @ou.setter
    def ou(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ou", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        The parentId of the imported account.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)


@pulumi.input_type
class OrganizationArgsArgs:
    def __init__(__self__, *,
                 accounts: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgsArgs']]]] = None,
                 enabled_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feature_set: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input['OrganizationPoliciesArgsArgs']] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgsArgs']]] accounts: The list of AWS Account to be configured in the Organization.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_policies: The list of enabled Organizations Policies in the organization.
        :param pulumi.Input[str] feature_set: The FeatureSet in the Organization..
        :param pulumi.Input[str] organization_id: The organization ID to import the Organization in the stack. If not set a new AWS Organization will be created. Defaults to undefined.
        :param pulumi.Input['OrganizationPoliciesArgsArgs'] policies: The Organization policies to be applied.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] services: The list of AWS Service Access Principals enabled in the organization.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if enabled_policies is not None:
            pulumi.set(__self__, "enabled_policies", enabled_policies)
        if feature_set is not None:
            pulumi.set(__self__, "feature_set", feature_set)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if services is not None:
            pulumi.set(__self__, "services", services)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgsArgs']]]]:
        """
        The list of AWS Account to be configured in the Organization.
        """
        return pulumi.get(self, "accounts")

    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OrganizationAccountArgsArgs']]]]):
        pulumi.set(self, "accounts", value)

    @property
    @pulumi.getter(name="enabledPolicies")
    def enabled_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of enabled Organizations Policies in the organization.
        """
        return pulumi.get(self, "enabled_policies")

    @enabled_policies.setter
    def enabled_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_policies", value)

    @property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> Optional[pulumi.Input[str]]:
        """
        The FeatureSet in the Organization..
        """
        return pulumi.get(self, "feature_set")

    @feature_set.setter
    def feature_set(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feature_set", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The organization ID to import the Organization in the stack. If not set a new AWS Organization will be created. Defaults to undefined.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input['OrganizationPoliciesArgsArgs']]:
        """
        The Organization policies to be applied.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input['OrganizationPoliciesArgsArgs']]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of AWS Service Access Principals enabled in the organization.
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "services", value)


@pulumi.input_type
class OrganizationPoliciesArgsArgs:
    def __init__(__self__, *,
                 deny_leave_organization: Optional[pulumi.Input['OrganizationPolicyArgsArgs']] = None):
        """
        :param pulumi.Input['OrganizationPolicyArgsArgs'] deny_leave_organization: Deny IAM Account to leave the organization. Enabled by default.
        """
        if deny_leave_organization is not None:
            pulumi.set(__self__, "deny_leave_organization", deny_leave_organization)

    @property
    @pulumi.getter(name="denyLeaveOrganization")
    def deny_leave_organization(self) -> Optional[pulumi.Input['OrganizationPolicyArgsArgs']]:
        """
        Deny IAM Account to leave the organization. Enabled by default.
        """
        return pulumi.get(self, "deny_leave_organization")

    @deny_leave_organization.setter
    def deny_leave_organization(self, value: Optional[pulumi.Input['OrganizationPolicyArgsArgs']]):
        pulumi.set(self, "deny_leave_organization", value)


@pulumi.input_type
class OrganizationPolicyArgsArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enabled: Enable the policy/
        :param pulumi.Input[str] policy_id: Import the policy with the given id
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable the policy/
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        Import the policy with the given id
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)


