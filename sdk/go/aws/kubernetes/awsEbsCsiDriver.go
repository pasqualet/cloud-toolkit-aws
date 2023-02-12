// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kubernetes

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AwsEbsCsiDriver struct {
	pulumi.ResourceState

	Application apiextensions.CustomResourceOutput `pulumi:"application"`
	Irsa        IrsaOutput                         `pulumi:"irsa"`
	Namespace   corev1.NamespaceOutput             `pulumi:"namespace"`
}

// NewAwsEbsCsiDriver registers a new resource with the given unique name, arguments, and options.
func NewAwsEbsCsiDriver(ctx *pulumi.Context,
	name string, args *AwsEbsCsiDriverArgs, opts ...pulumi.ResourceOption) (*AwsEbsCsiDriver, error) {
	if args == nil {
		args = &AwsEbsCsiDriverArgs{}
	}

	opts = pkgResourceDefaultOpts(opts)
	var resource AwsEbsCsiDriver
	err := ctx.RegisterRemoteComponentResource("cloud-toolkit-aws:kubernetes:AwsEbsCsiDriver", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type awsEbsCsiDriverArgs struct {
}

// The set of arguments for constructing a AwsEbsCsiDriver resource.
type AwsEbsCsiDriverArgs struct {
}

func (AwsEbsCsiDriverArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*awsEbsCsiDriverArgs)(nil)).Elem()
}

type AwsEbsCsiDriverInput interface {
	pulumi.Input

	ToAwsEbsCsiDriverOutput() AwsEbsCsiDriverOutput
	ToAwsEbsCsiDriverOutputWithContext(ctx context.Context) AwsEbsCsiDriverOutput
}

func (*AwsEbsCsiDriver) ElementType() reflect.Type {
	return reflect.TypeOf((**AwsEbsCsiDriver)(nil)).Elem()
}

func (i *AwsEbsCsiDriver) ToAwsEbsCsiDriverOutput() AwsEbsCsiDriverOutput {
	return i.ToAwsEbsCsiDriverOutputWithContext(context.Background())
}

func (i *AwsEbsCsiDriver) ToAwsEbsCsiDriverOutputWithContext(ctx context.Context) AwsEbsCsiDriverOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AwsEbsCsiDriverOutput)
}

// AwsEbsCsiDriverArrayInput is an input type that accepts AwsEbsCsiDriverArray and AwsEbsCsiDriverArrayOutput values.
// You can construct a concrete instance of `AwsEbsCsiDriverArrayInput` via:
//
//	AwsEbsCsiDriverArray{ AwsEbsCsiDriverArgs{...} }
type AwsEbsCsiDriverArrayInput interface {
	pulumi.Input

	ToAwsEbsCsiDriverArrayOutput() AwsEbsCsiDriverArrayOutput
	ToAwsEbsCsiDriverArrayOutputWithContext(context.Context) AwsEbsCsiDriverArrayOutput
}

type AwsEbsCsiDriverArray []AwsEbsCsiDriverInput

func (AwsEbsCsiDriverArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AwsEbsCsiDriver)(nil)).Elem()
}

func (i AwsEbsCsiDriverArray) ToAwsEbsCsiDriverArrayOutput() AwsEbsCsiDriverArrayOutput {
	return i.ToAwsEbsCsiDriverArrayOutputWithContext(context.Background())
}

func (i AwsEbsCsiDriverArray) ToAwsEbsCsiDriverArrayOutputWithContext(ctx context.Context) AwsEbsCsiDriverArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AwsEbsCsiDriverArrayOutput)
}

// AwsEbsCsiDriverMapInput is an input type that accepts AwsEbsCsiDriverMap and AwsEbsCsiDriverMapOutput values.
// You can construct a concrete instance of `AwsEbsCsiDriverMapInput` via:
//
//	AwsEbsCsiDriverMap{ "key": AwsEbsCsiDriverArgs{...} }
type AwsEbsCsiDriverMapInput interface {
	pulumi.Input

	ToAwsEbsCsiDriverMapOutput() AwsEbsCsiDriverMapOutput
	ToAwsEbsCsiDriverMapOutputWithContext(context.Context) AwsEbsCsiDriverMapOutput
}

type AwsEbsCsiDriverMap map[string]AwsEbsCsiDriverInput

func (AwsEbsCsiDriverMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AwsEbsCsiDriver)(nil)).Elem()
}

func (i AwsEbsCsiDriverMap) ToAwsEbsCsiDriverMapOutput() AwsEbsCsiDriverMapOutput {
	return i.ToAwsEbsCsiDriverMapOutputWithContext(context.Background())
}

func (i AwsEbsCsiDriverMap) ToAwsEbsCsiDriverMapOutputWithContext(ctx context.Context) AwsEbsCsiDriverMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AwsEbsCsiDriverMapOutput)
}

type AwsEbsCsiDriverOutput struct{ *pulumi.OutputState }

func (AwsEbsCsiDriverOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AwsEbsCsiDriver)(nil)).Elem()
}

func (o AwsEbsCsiDriverOutput) ToAwsEbsCsiDriverOutput() AwsEbsCsiDriverOutput {
	return o
}

func (o AwsEbsCsiDriverOutput) ToAwsEbsCsiDriverOutputWithContext(ctx context.Context) AwsEbsCsiDriverOutput {
	return o
}

func (o AwsEbsCsiDriverOutput) Application() apiextensions.CustomResourceOutput {
	return o.ApplyT(func(v *AwsEbsCsiDriver) apiextensions.CustomResourceOutput { return v.Application }).(apiextensions.CustomResourceOutput)
}

func (o AwsEbsCsiDriverOutput) Irsa() IrsaOutput {
	return o.ApplyT(func(v *AwsEbsCsiDriver) IrsaOutput { return v.Irsa }).(IrsaOutput)
}

func (o AwsEbsCsiDriverOutput) Namespace() corev1.NamespaceOutput {
	return o.ApplyT(func(v *AwsEbsCsiDriver) corev1.NamespaceOutput { return v.Namespace }).(corev1.NamespaceOutput)
}

type AwsEbsCsiDriverArrayOutput struct{ *pulumi.OutputState }

func (AwsEbsCsiDriverArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AwsEbsCsiDriver)(nil)).Elem()
}

func (o AwsEbsCsiDriverArrayOutput) ToAwsEbsCsiDriverArrayOutput() AwsEbsCsiDriverArrayOutput {
	return o
}

func (o AwsEbsCsiDriverArrayOutput) ToAwsEbsCsiDriverArrayOutputWithContext(ctx context.Context) AwsEbsCsiDriverArrayOutput {
	return o
}

func (o AwsEbsCsiDriverArrayOutput) Index(i pulumi.IntInput) AwsEbsCsiDriverOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AwsEbsCsiDriver {
		return vs[0].([]*AwsEbsCsiDriver)[vs[1].(int)]
	}).(AwsEbsCsiDriverOutput)
}

type AwsEbsCsiDriverMapOutput struct{ *pulumi.OutputState }

func (AwsEbsCsiDriverMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AwsEbsCsiDriver)(nil)).Elem()
}

func (o AwsEbsCsiDriverMapOutput) ToAwsEbsCsiDriverMapOutput() AwsEbsCsiDriverMapOutput {
	return o
}

func (o AwsEbsCsiDriverMapOutput) ToAwsEbsCsiDriverMapOutputWithContext(ctx context.Context) AwsEbsCsiDriverMapOutput {
	return o
}

func (o AwsEbsCsiDriverMapOutput) MapIndex(k pulumi.StringInput) AwsEbsCsiDriverOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AwsEbsCsiDriver {
		return vs[0].(map[string]*AwsEbsCsiDriver)[vs[1].(string)]
	}).(AwsEbsCsiDriverOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AwsEbsCsiDriverInput)(nil)).Elem(), &AwsEbsCsiDriver{})
	pulumi.RegisterInputType(reflect.TypeOf((*AwsEbsCsiDriverArrayInput)(nil)).Elem(), AwsEbsCsiDriverArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AwsEbsCsiDriverMapInput)(nil)).Elem(), AwsEbsCsiDriverMap{})
	pulumi.RegisterOutputType(AwsEbsCsiDriverOutput{})
	pulumi.RegisterOutputType(AwsEbsCsiDriverArrayOutput{})
	pulumi.RegisterOutputType(AwsEbsCsiDriverMapOutput{})
}
