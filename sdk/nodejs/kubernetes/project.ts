// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

import * as pulumiKubernetes from "@pulumi/kubernetes";

/**
 * Project is a component that create the resources in the Cluster for a set of AWS IAM Users and Roles, manging the access with the integration with AWS IAM.
 */
export class Project extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'cloud-toolkit-aws:kubernetes:Project';

    /**
     * Returns true if the given object is an instance of Project.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Project {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Project.__pulumiType;
    }

    /**
     * The Kubernetes RoleBinding for admin users.
     */
    public /*out*/ readonly adminRoleBinding!: pulumi.Output<pulumiKubernetes.rbac.v1.RoleBinding>;
    /**
     * The Kubernetes ClusterRole used to grant minimal access to the cluster.
     */
    public /*out*/ readonly clusterRole!: pulumi.Output<pulumiKubernetes.rbac.v1.ClusterRole>;
    /**
     * The Kubernetes ClusterRoleBinding to associate the ClusterRole to the project.
     */
    public /*out*/ readonly clusterRoleBinding!: pulumi.Output<pulumiKubernetes.rbac.v1.ClusterRoleBinding>;
    /**
     * The Kubernetes RoleBinding for edit users.
     */
    public /*out*/ readonly editRoleBinding!: pulumi.Output<pulumiKubernetes.rbac.v1.RoleBinding>;
    /**
     * The Namespace used by the project.
     */
    public readonly namespace!: pulumi.Output<pulumiKubernetes.core.v1.Namespace>;
    /**
     * The Kubernetes provider used to provision Kubernetes resources.
     */
    public /*out*/ readonly provider!: pulumi.Output<pulumiKubernetes.Provider>;
    /**
     * ResourceQuota for the provisioned Namespace.
     */
    public /*out*/ readonly resourceQuota!: pulumi.Output<pulumiKubernetes.core.v1.ResourceQuota>;
    /**
     * The Kubernetes RoleBinding for view users.
     */
    public /*out*/ readonly viewRoleBinding!: pulumi.Output<pulumiKubernetes.rbac.v1.RoleBinding>;

    /**
     * Create a Project resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProjectArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.kubeconfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'kubeconfig'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.namespace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'namespace'");
            }
            resourceInputs["adminUserArns"] = args ? args.adminUserArns : undefined;
            resourceInputs["editUserArns"] = args ? args.editUserArns : undefined;
            resourceInputs["kubeconfig"] = args ? args.kubeconfig : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["namespace"] = args ? args.namespace : undefined;
            resourceInputs["resources"] = args ? args.resources : undefined;
            resourceInputs["viewUserArns"] = args ? args.viewUserArns : undefined;
            resourceInputs["adminRoleBinding"] = undefined /*out*/;
            resourceInputs["clusterRole"] = undefined /*out*/;
            resourceInputs["clusterRoleBinding"] = undefined /*out*/;
            resourceInputs["editRoleBinding"] = undefined /*out*/;
            resourceInputs["provider"] = undefined /*out*/;
            resourceInputs["resourceQuota"] = undefined /*out*/;
            resourceInputs["viewRoleBinding"] = undefined /*out*/;
        } else {
            resourceInputs["adminRoleBinding"] = undefined /*out*/;
            resourceInputs["clusterRole"] = undefined /*out*/;
            resourceInputs["clusterRoleBinding"] = undefined /*out*/;
            resourceInputs["editRoleBinding"] = undefined /*out*/;
            resourceInputs["namespace"] = undefined /*out*/;
            resourceInputs["provider"] = undefined /*out*/;
            resourceInputs["resourceQuota"] = undefined /*out*/;
            resourceInputs["viewRoleBinding"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Project.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a Project resource.
 */
export interface ProjectArgs {
    /**
     * The list of AWS IAM User arns that can access to this project with 'admin' role.
     */
    adminUserArns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The list of AWS IAM User arns that can access to this project with 'edit' role.
     */
    editUserArns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Kubernetes provider used by Pulumi.
     */
    kubeconfig: pulumi.Input<string>;
    /**
     * The Project name.
     */
    name: pulumi.Input<string>;
    /**
     * The Namespace name where the addon will be installed.
     */
    namespace: pulumi.Input<string>;
    /**
     * The cluster resources to be assigned to the project.
     */
    resources?: pulumi.Input<inputs.kubernetes.ProjectResourcesArgsArgs>;
    /**
     * The list of AWS IAM User arns that can access to this project with 'view' role.
     */
    viewUserArns?: pulumi.Input<pulumi.Input<string>[]>;
}
