// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package landingzone

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/organizations"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Organization is the component that configure the AWS Orgazination, AWS Accounts and AWS Organization Policies.
type Organization struct {
	pulumi.ResourceState

	// The list of AWS Accounts inside the Organization.
	AccountIds pulumi.StringArrayOutput `pulumi:"accountIds"`
	// The list of AWS Provider for the managed accounts by this component.
	AccountProviders OrganizationAccountProviderMappingArrayOutput `pulumi:"accountProviders"`
	// The list of Accounts.
	Accounts AccountMappingArrayOutput `pulumi:"accounts"`
	// The AWS Organization.
	Organization organizations.OrganizationOutput `pulumi:"organization"`
	// The list Organizatoinal Units.
	OrganizationalUnits OrganizationalUnitMappingArrayOutput `pulumi:"organizationalUnits"`
	// The list of Policies used in the Organization.
	Policies organizations.PolicyArrayOutput `pulumi:"policies"`
	// The list of Policy Attachments used in the Organization.
	PolicyAttachments organizations.PolicyAttachmentArrayOutput `pulumi:"policyAttachments"`
}

// NewOrganization registers a new resource with the given unique name, arguments, and options.
func NewOrganization(ctx *pulumi.Context,
	name string, args *OrganizationArgs, opts ...pulumi.ResourceOption) (*Organization, error) {
	if args == nil {
		args = &OrganizationArgs{}
	}

	opts = pkgResourceDefaultOpts(opts)
	var resource Organization
	err := ctx.RegisterRemoteComponentResource("cloud-toolkit-aws:landingzone:Organization", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type organizationArgs struct {
	// The list of AWS Account to be configured in the Organization.
	Accounts []OrganizationAccount `pulumi:"accounts"`
	// The list of enabled Organizations Policies in the organization.
	EnabledPolicies []string `pulumi:"enabledPolicies"`
	// The FeatureSet in the Organization..
	FeatureSet *string `pulumi:"featureSet"`
	// The organization ID to import the Organization in the stack. If not set a new AWS Organization will be created. Defaults to undefined.
	OrganizationId *string `pulumi:"organizationId"`
	// The Organization policies to be applied.
	Policies *OrganizationPolicies `pulumi:"policies"`
	// The list of AWS Service Access Principals enabled in the organization.
	Services []string `pulumi:"services"`
}

// The set of arguments for constructing a Organization resource.
type OrganizationArgs struct {
	// The list of AWS Account to be configured in the Organization.
	Accounts OrganizationAccountArrayInput
	// The list of enabled Organizations Policies in the organization.
	EnabledPolicies pulumi.StringArrayInput
	// The FeatureSet in the Organization..
	FeatureSet pulumi.StringPtrInput
	// The organization ID to import the Organization in the stack. If not set a new AWS Organization will be created. Defaults to undefined.
	OrganizationId pulumi.StringPtrInput
	// The Organization policies to be applied.
	Policies OrganizationPoliciesPtrInput
	// The list of AWS Service Access Principals enabled in the organization.
	Services pulumi.StringArrayInput
}

func (OrganizationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationArgs)(nil)).Elem()
}

type OrganizationInput interface {
	pulumi.Input

	ToOrganizationOutput() OrganizationOutput
	ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput
}

func (*Organization) ElementType() reflect.Type {
	return reflect.TypeOf((**Organization)(nil)).Elem()
}

func (i *Organization) ToOrganizationOutput() OrganizationOutput {
	return i.ToOrganizationOutputWithContext(context.Background())
}

func (i *Organization) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationOutput)
}

// OrganizationArrayInput is an input type that accepts OrganizationArray and OrganizationArrayOutput values.
// You can construct a concrete instance of `OrganizationArrayInput` via:
//
//	OrganizationArray{ OrganizationArgs{...} }
type OrganizationArrayInput interface {
	pulumi.Input

	ToOrganizationArrayOutput() OrganizationArrayOutput
	ToOrganizationArrayOutputWithContext(context.Context) OrganizationArrayOutput
}

type OrganizationArray []OrganizationInput

func (OrganizationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Organization)(nil)).Elem()
}

func (i OrganizationArray) ToOrganizationArrayOutput() OrganizationArrayOutput {
	return i.ToOrganizationArrayOutputWithContext(context.Background())
}

func (i OrganizationArray) ToOrganizationArrayOutputWithContext(ctx context.Context) OrganizationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationArrayOutput)
}

// OrganizationMapInput is an input type that accepts OrganizationMap and OrganizationMapOutput values.
// You can construct a concrete instance of `OrganizationMapInput` via:
//
//	OrganizationMap{ "key": OrganizationArgs{...} }
type OrganizationMapInput interface {
	pulumi.Input

	ToOrganizationMapOutput() OrganizationMapOutput
	ToOrganizationMapOutputWithContext(context.Context) OrganizationMapOutput
}

type OrganizationMap map[string]OrganizationInput

func (OrganizationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Organization)(nil)).Elem()
}

func (i OrganizationMap) ToOrganizationMapOutput() OrganizationMapOutput {
	return i.ToOrganizationMapOutputWithContext(context.Background())
}

func (i OrganizationMap) ToOrganizationMapOutputWithContext(ctx context.Context) OrganizationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationMapOutput)
}

type OrganizationOutput struct{ *pulumi.OutputState }

func (OrganizationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Organization)(nil)).Elem()
}

func (o OrganizationOutput) ToOrganizationOutput() OrganizationOutput {
	return o
}

func (o OrganizationOutput) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return o
}

// The list of AWS Accounts inside the Organization.
func (o OrganizationOutput) AccountIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Organization) pulumi.StringArrayOutput { return v.AccountIds }).(pulumi.StringArrayOutput)
}

// The list of AWS Provider for the managed accounts by this component.
func (o OrganizationOutput) AccountProviders() OrganizationAccountProviderMappingArrayOutput {
	return o.ApplyT(func(v *Organization) OrganizationAccountProviderMappingArrayOutput { return v.AccountProviders }).(OrganizationAccountProviderMappingArrayOutput)
}

// The list of Accounts.
func (o OrganizationOutput) Accounts() AccountMappingArrayOutput {
	return o.ApplyT(func(v *Organization) AccountMappingArrayOutput { return v.Accounts }).(AccountMappingArrayOutput)
}

// The AWS Organization.
func (o OrganizationOutput) Organization() organizations.OrganizationOutput {
	return o.ApplyT(func(v *Organization) organizations.OrganizationOutput { return v.Organization }).(organizations.OrganizationOutput)
}

// The list Organizatoinal Units.
func (o OrganizationOutput) OrganizationalUnits() OrganizationalUnitMappingArrayOutput {
	return o.ApplyT(func(v *Organization) OrganizationalUnitMappingArrayOutput { return v.OrganizationalUnits }).(OrganizationalUnitMappingArrayOutput)
}

// The list of Policies used in the Organization.
func (o OrganizationOutput) Policies() organizations.PolicyArrayOutput {
	return o.ApplyT(func(v *Organization) organizations.PolicyArrayOutput { return v.Policies }).(organizations.PolicyArrayOutput)
}

// The list of Policy Attachments used in the Organization.
func (o OrganizationOutput) PolicyAttachments() organizations.PolicyAttachmentArrayOutput {
	return o.ApplyT(func(v *Organization) organizations.PolicyAttachmentArrayOutput { return v.PolicyAttachments }).(organizations.PolicyAttachmentArrayOutput)
}

type OrganizationArrayOutput struct{ *pulumi.OutputState }

func (OrganizationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Organization)(nil)).Elem()
}

func (o OrganizationArrayOutput) ToOrganizationArrayOutput() OrganizationArrayOutput {
	return o
}

func (o OrganizationArrayOutput) ToOrganizationArrayOutputWithContext(ctx context.Context) OrganizationArrayOutput {
	return o
}

func (o OrganizationArrayOutput) Index(i pulumi.IntInput) OrganizationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Organization {
		return vs[0].([]*Organization)[vs[1].(int)]
	}).(OrganizationOutput)
}

type OrganizationMapOutput struct{ *pulumi.OutputState }

func (OrganizationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Organization)(nil)).Elem()
}

func (o OrganizationMapOutput) ToOrganizationMapOutput() OrganizationMapOutput {
	return o
}

func (o OrganizationMapOutput) ToOrganizationMapOutputWithContext(ctx context.Context) OrganizationMapOutput {
	return o
}

func (o OrganizationMapOutput) MapIndex(k pulumi.StringInput) OrganizationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Organization {
		return vs[0].(map[string]*Organization)[vs[1].(string)]
	}).(OrganizationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationInput)(nil)).Elem(), &Organization{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationArrayInput)(nil)).Elem(), OrganizationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationMapInput)(nil)).Elem(), OrganizationMap{})
	pulumi.RegisterOutputType(OrganizationOutput{})
	pulumi.RegisterOutputType(OrganizationArrayOutput{})
	pulumi.RegisterOutputType(OrganizationMapOutput{})
}
