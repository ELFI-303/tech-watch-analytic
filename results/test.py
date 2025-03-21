cloud_computing_terms = [
    "aws", "azure", "gcp", "ec2", "s3", "lambda", "ecs", "eks", "fargate", "batch", 
    "lightsail", "route53", "cloudfront", "cloudformation", "rds", "aurora", "dynamodb", 
    "redshift", "elasticache", "neptune", "sagemaker", "rekognition", "comprehend", "textract", 
    "polly", "transcribe", "emr", "sns", "sqs", "cognito", "athena", "kinesis", "ddb", "ssm", 
    "eksctl", "ecr", "kms", "waf", "acm", "vpc", "iam", "api", "sdk", "cli", "cdk", "sam", 
    "cloudwatch", "s3a", "sts", "snowball", "fsx", "glacier", "elasticloadbalancer", "swf", 
    "lambda@edge", "r53", "lex", "polly", "transcribe", "ebs", "efs", "dms", "ecs", "eks", 
    "sqs", "vms", "t2", "gpu", "t3", "on-demand", "elasticsearch", "vpc", "bastion", "vms", 
    "vcpu", "region", "availabilityzone", "zone", "edge", "cli", "sdk", "eks", "cloudtrail", 
    "cloudwatch", "lambda@edge", "gateway", "vpn", "directconnect", "route53", "boto3", 
    "autoscaling", "terraform", "k8s", "dynamodb", "kinesis", "fargate", "s3", "ec2", "vpc", 
    "subnet", "cidr", "natgateway", "firewall", "vpn", "loadbalancer", "lb", "acl", "routing", 
    "dns", "dhcp", "nsg", "bgp", "pppoe", "ipsec", "vpn_tunnel", "overlay_network", "ecmp", 
    "next-hop", "networkinterface", "iptables", "l3", "firewallrule", "wan", "lan", "ipv6", 
    "ipv4", "osfp", "iptables", "vlan", "ssl", "tls", "edge_gateway", "vpn_server", "dhcp_server", 
    "dhcp_relay", "cloudrouter", "apigateway", "routetable", "gw", "vpnclient", "vpnserver", 
    "routepropagation", "loadbalancer", "natgateway", "aclrule", "networkmanager", "peering", 
    "4g", "5g", "geolocation", "networktopology", "firewalld", "proxy", "dnsserver", "dhcpd", 
    "cloudnat", "peeringconnection", "loadbalancer", "vms", "mtu", "stateful", "stateless", 
    "radius", "ssid", "ntp", "qos", "certificate", "keypair", "pki", "ipsectunnel", "sslvpn", 
    "openvpn", "dhcplease", "dhcpclient", "dhcpoption", "ssh", "publickey", "privatekey", 
    "meshnetwork", "multicast", "api_key", "endpoint", "whitelisting", "blacklisting", "accessgroup", 
    "usergroup", "policy", "userroles", "authentication", "authorization", "identity", "securitypatch", 
    "firewalls", "vms", "tpm", "cybersecurity", "patching", "apisecurity", "federatedidentity", 
    "oauth", "adfs", "bastionhost", "keymanagement", "cmk", "cspm", "sim", "securitygroup", "waf", 
    "hsts", "sdlc", "risk", "threat", "vulnerability", "compliance", "cis", "auditlog", "reporting", 
    "eventlog", "malware", "ransomware", "honeypot", "accesspoint", "cyberevent", "firewalllogs", 
    "deeppacketinspection", "whitelisting", "tcpdump", "intrusiondetection", "intrusionprevention", 
    "tlscert", "ssl", "ssh", "mfa", "two-factor", "rsa", "cert", "pem", "pkcs", "asymmetric", 
    "symmetric", "crypto", "sid", "hashing", "sha256", "sha512", "ca", "firewall", "vpn", "encryption", 
    "tls", "https", "mfa", "oauth", "rsa", "jwt", "asymmetric", "symmetric", "pki", "oauth", "tls", 
    "firewall", "waf", "cloud", "cloudsecurity", "backup", "restore", "snapshot", "raid", "file", 
    "volume", "vms", "storage", "disk", "cloudblock", "ssd", "hdd", "deduplication", "replication", 
    "coldstorage", "hotstorage", "tieredstorage", "cache", "bandwidth", "cluster", "storageclass", 
    "offload", "onlinestorage", "backuppolicy", "dataprotection", "file", "rsync", "fileserver", 
    "backend", "coldbackup", "hotbackup", "rto", "rpo", "mountpoint", "cloudvolume", "file_sync", 
    "sql", "nosql", "postgresql", "mongodb", "redis", "cassandra", "firebase", "bigquery", "sqlite", 
    "mysql", "hbase", "couchdb", "cloudsql", "schema", "index", "table", "query", "join", "insert", 
    "update", "delete", "select", "rollback", "commit", "trigger", "view", "api", "migration", 
    "replication", "dbcluster", "nosql", "sharding", "primarykey", "secondaryindex", "column", 
    "dbengine", "normalization", "denormalization", "acisql", "dbaaS", "multitenant", "polygot", 
    "database_scaling", "shardeddatabase", "nonrelational", "keyvalue", "relational", "databaseperformance", 
    "datastore", "indexing", "clouddb", "inmemorydb", "databasebackup", "dbtuning", "unit", "integration", 
    "functional", "unit-test", "integration-test", "e2e-test", "testing", "cicd", "jenkins", "gitlab", 
    "github", "git", "branch", "commit", "merge", "pullrequest", "push", "workflow", "container", 
    "containerization", "microservice", "cluster", "automation", "ansible", "docker", "kubernetes", 
    "helm", "terraform", "yaml", "json", "build", "testing", "quality", "delivery", "monitoring", 
    "alerting", "logging", "deployment", "logging", "dev", "staging", "prod", "parity", "release", 
    "task", "feature", "deploy", "monitor", "healthcheck", "api", "web", "api_gateway", "containerd", 
    "devops", "cicd", "devopsautomation", "vpc", "iam", "docker", "api_request", "cloudapi", "serverless", 
    "function", "event", "failover", "clouddisk", "cloudfile", "api_gateway", "server", "proxy", "eventdriven",  
    "server", "client", "app", "webapp", "webservice", "cloudstorage", "dbms", "framework", "node", 
    "machine", "network", "apiendpoint", "rest", "soap", "rpc", "tcp", "udp", "http", "https", "ip", 
    "ipv4", "ipv6", "eth", "ethernet", "networkinterface", "socket", "vlan", "firewall", "proxy", 
    "subnet", "gateway", "loadbalancer", "cdn", "tunnel", "gateway", "acl", "routing", "router", 
    "dnsserver", "dhcp", "syslog", "auditlog", "session", "cookies", "tlsencryption", "httpsrequest", 
    "httpresponse", "corerouter", "edgegateway", "dataplane", "controlplane", "cloudrouter", "rack", 
    "cluster", "racks", "datacenter", "opticalfiber", "connection", "port", "spectrum", "broadband", 
    "bandwidth", "protocol", "node", "instance", "platform", "region", "availability", "recovery", 
    "scaling", "resilience", "redundancy", "highavailability", "loadbalancing", "service", "microservice", 
    "rpc", "event", "cloudmesh", "eventdriven", "docker", "kubernetes", "container", "vmware", "devops", 
    "ci", "cd", "cicd", "git", "jenkins", "travis", "bitbucket", "pipelines", "github", "gitlab", "workflow", 
    "devopsengineer", "jenkinsfile", "gitflow", "terraform", "helm", "azuredevops", "ansible", "puppet", 
    "saltstack", "cloudformation", "awscli", "rdsbackup", "dbbackup", "backup", "restore", "snapshot", 
    "datadump", "scaleout", "replication", "failover", "continuousintegration", "continuousdelivery", 
    "continuousdeployment", "automation", "monitoring", "alert", "log", "logging", "metrics", "dashboard", 
    "observability", "performance", "loadtest", "stresstest", "profiling", "latency", "latencytest", 
    "throughput", "response", "request", "caching", "contentdelivery", "dynamic", "static", "autoscaling", 
    "cluster", "gpu", "cpu", "ram", "hdd", "ssd", "datastore", "datashard", "nosql", "relational", "schema", 
    "database", "containerization", "orchestration", "workflow", "eventstream", "datastream", "dataflow", 
    "bucket", "serviceaccount", "appdeployment", "virtualmachine", "vms", "containerservice", "cloudhost", 
    "cpu", "disk", "cloudapps", "storagesystem", "webservice", "deployment", "serviceapi", "apiaccess", 
    "autodeploy", "cloudinstance", "containerhost", "deploymentzone", "upstream", "downstream", "multi-tenancy", 
    "datacenter", "switch", "router", "nfs", "device", "datapool", "multicloud", "multivm", "hybridcloud", 
    "edgecomputing", "dataprocessing", "computation", "hypervisor", "virtualization", "desktopasS", "publiccloud", 
    "privatecloud", "cloudformation", "multicloud", "cloudnative", "resourceallocation", "onpremise", "databaseasS", 
    "computeasS", "containerasS", "iaas", "paas", "saas", "iotcloud", "backuptas", "virtualnetwork", "vpc", 
    "sshmessaging", "tcpconnection", "ssllock", "databasecluster", "instancegroup", "cascading", "scalability", 
    "scalabledb", "memcached", "couchbase", "cloudnative", "containerd", "e2e", "containerapp", "edgegateway", 
    "cspm", "paas", "webservices", "eventbus", "flow", "file", "backupcloud", "computeunit", "dbcluster", 
    "isolation", "monitoringapi", "threatintel", "userdataprotection", "spectrum", "threatdetection", "networktap", 
    "mdm", "sandbox", "quarantine", "nextgenfirewall", "edgefirewall", "endpoint", "cloudsecurity", "networkpolicy", 
    "dataaccess", "cloudnetwork", "encryptionkey", "apiresponse", "routingpolicy", "cloudkey", "ticketing", 
    "queue", "clouddrive", "backuptarget", "computecloud", "containerlogs", "datavolume", "dbmonitoring", 
    "datacentre", "gatewayapi", "iamrole", "vmsmigration", "distributed", "privileged", "proxyconfig", "loadbalancer", 
    "backendsystem", "resourcepool", "directconnect", "fileobject", "sync", "migration", "logging", "objectstorage", 
    "cache", "auth", "cryptography", "resource", "cloudfunction", "databreach", "performancemetrics", "asynchrounous", 
    "failovercluster", "cloudedge", "interconnect", "cloudmanagement", "cloudtool", "deploymentzone", "dbcloud", 
    "cloudbroker", "storagepool", "datamigration", "usergroup", "uploader", "cloudresources", "datateam", 
    "softwarecontainer", "multitenant", "cloudvpn", "systemintegration", "dataengineering", "projectmanager", 
    "virtualization", "edgemachine", "objectid", "metadata", "datagovernance", "replicationcluster", "netbackup", 
    "containerservice", "cloudcomputing", "continuousmonitoring", "hypervisorcluster", "s3bucket", "cloudconsole", 
    "projectid", "credential", "sysadmin", "datastore", "job", "notification", "cloudrepository", "remoteaccess", 
    "ai", "ml", "iot", "api", "gpu", "cpu", "ram", "dns", "lan", "wan", "url",
    "gb", "tb", "kb", "mb", "ms", "ns",
    "cmd", "log", "dev", "var",
    "vpc", "iam", "cli", "sdk", "os", "db", "ssh", "tls",
    "aws", "gcp", "saas", "paas", "iaas", "vm", "sla",
    "ip", "mac", "uid", "pid", "id", "aas","sql","cicd", "ci", "cd",
    "orchestration", "bastion", "edge", "scalable", "container"
    # AWS terms
    "ec2", "ecs", "eks", "lambda", "fargate", "batch", "lightsail",
    "s3", "ebs", "efs", "glacier", "fsx", "snowball", "route53", "cloudfront",
    "rds", "aurora", "dynamodb", "redshift", "elasticache", "neptune",
    "sagemaker", "rekognition", "comprehend", "textract", "polly", "transcribe",
    "cloudformation", "cloudwatch", "sns", "sqs", "cognito", "athena", "kinesis",
    "ddb", "rs", "dms", "elb", "cf", "r53", "kms", "waf", "acm", "emr",
    "kda", "kds", "kdf", "sqs", "ses", "swf", "cfn", "cw", "cwe","lz"
    "cwl", "cli", "sdk", "sam", "cdk", "sms", "ds", "lex", "iot","sct",
    "ecr", "eksctl", "ssm", "s3a"
    # Azure terms
    "vm", "aks", "sql", "cos", "dns", "nsg", "lb", "vpn", "aad", 
    "kms", "arm", "cli", "sdk", "dls", "sb", "eh", "msi", "vnet", 
    "rds", "ad", "api", "bse", "wvd", "fs", "hci", "dfs", "hdi", 
    "iam", "ntp", "api", "asp", "cns", "cdn", "crr", "ci", "sts", 
    "tfs", "sec", "spn", "ssl", "tls", "waf", "bkg", "acr", "sso", 
    "tpm", "vms", "log", "prv", "rdp", "mfa", "sts", "atp", "mc","adfs",
    "aci", "asr", "rbac", "rg"
    # GCP terms
    "gce", "gke", "gcs", "sql", "vpc", "iam", "kms", "iap", "bq", 
    "tpu", "cli", "dns", "hpc", "bq", "ps", "api", "vmf", "gcs", 
    "cf", "pdk", "csp", "cds", "dms", "gcl", "bkt", "bfp", "bsa", 
    "bvs", "gcf", "gcs", "gsd", "gsf", "gke", "gsb", "bks", "gdb", 
    "bws", "tce", "vms", "sst", "psp", "gke", "gcb","pubsub", "compute",
    "virtualbox", "virtualmachine", "dockerimage", "kubernetescluster", "serverlessarchitecture",
    "edgecomputing", "multicloudstrategy", "containerorchestration", "serverinstantiation", "hyperconverged",
    "softwaredefined", "containerdeployment", "platformasaservice", "cloudstoragegateway", "storagecontainer",
    "dataintegration", "datawarehouse", "computinginstance", "infrastructuremanagement", "cloudworkflow",
    "cloudmigration", "cloudhosted", "cloudplatform", "virtualnetworking", "applicationdeployment",
    "devopsautomation", "continuousintegrationdeployment", "devopsservices", "cloudprovisioning", "terraformplan",
    "azurecloud", "googlecloud", "cloudapiendpoint", "cloudservicesintegration", "cloudinfrastructureascode",
    "servercluster", "softwareassets", "datacentermanagement", "eventdrivenarchitecture", "datacaching",
    "distributedcomputation", "cloudorchestration", "containerimage", "cloudsecops", "virtualizationtechnology",
    "dataaggregation", "cloudcontentdelivery", "networkinfrastructure", "faulttolerance", "endpointsecurity",
    "cloudsync", "autoenrollment", "cloudbasedsolution", "dynamiccloud", "cloudoperatingsystem",
    "osaservice", "cloudsecurityposture", "clouduserauthentication", "cloudfirewall", "logmanagement",
    "cloudidentifier", "unifiedcloudmanagement", "cloudconnectivity", "cloudscale", "disasterrecoveryplan",
    "loadbalancingservice", "networkmonitoring", "cloudbackupsystem", "encryptionatrest", "networklatency",
    "realtimenetworking", "applicationlogging", "cloudtrafficmanagement", "computingresource", "cloudtooling",
    "cloudsecurityarchitecture", "edgecomputingdevice", "networkrouting", "publickeyinfrastructure", "privatedatacenter",
    "cloudnativemicroservices", "apideployment", "cloudfailover", "computeengine", "workloadorchestration",
    "securecloudstorage", "cloudnativeplatform", "virtualserver", "dataexfiltration", "vmmanagement",
    "continuousdeploymentpipeline", "virtualdisk", "cloudtoolchain", "securitybestpractices", "cloudintegrationlayer",
    "workloadautomation", "datacenterautomation", "backupandsnapshot", "datamigrationplan", "cloudusageanalytics",
    "performanceoptimization", "cloudbursting", "encryptionprotocol", "multitenantarchitecture", "softwarestack",
    "virtualprivatecloud", "virtualdatacenter", "backupandrecovery", "dataencryption", "cloudresourcesmanagement",
    "serviceorchestration", "cloudservicecatalog", "distributedcomputingcluster", "cloudhpc", "infrastructureasacode",
    "cloudworkloadmanagement", "filedistribution", "advancedvirtualization", "distributedstorage", "datareplication",
    "cloudconfigmanagement", "dynamicprovisioning", "networkreliability", "intercloudconnectivity", "clouduserinterface",
    "seamlesscloudintegration", "highperformancedatastorage", "hybridcloudsolution", "containerclusterscaling", "cloudbackupstrategy",
    "filedatarepository", "networkpathmanagement", "elasticcomputing", "automatedscaling", "virtualservermanagement",
    "cloudlogging", "systemmonitoringtools", "cloudtroubleshooting", "orchestrationplatform", "dynamiccompute",
    "cloudauditlogs", "computeoptimization", "distributedfilemanagement", "edgeapplicationdeployment", "automatedcontainerdeployment",
    "cloudbackupservice", "useraccessmanagement", "virtualfilemanager", "cloudserviceorchestration", "cloudnativeworkloads",
    "serverorchestration", "hypervisorcloud", "automatedloadbalancing", "vmfailover", "virtualresourceallocation",
    "cloudbasedauthentication", "scalablecloudsolution", "edgecaching", "infrastructureprovisioning", "endpointprotection",
    "resourcepoolmanagement", "containerizeddeployment", "datadiskmount", "cloudserviceprovisioning", "loadbalanceroptimization",
    "elasticinfrastructure", "databaseclusterautoscaling", "servermanagementautomation", "cloudbasedinfrastructure", "containerfailover",
    "datacenterscaling", "hybridinfrastructure", "securityoperationscenter", "virtualinfrastructuremonitoring", "cloudlogaggregation",
    "edgecloudcomputing", "devopsanalytics", "datacontainerization", "publiccloudresource", "automatedserverprovisioning",
    "virtualdesktopinfrastructure", "continuousmonitoringplatform", "cloudoptimizationtool", "clusterformation", "edgecomputingsystem",
    "serverclustermanagement", "contentdeliverynetwork", "globalcloudinfrastructure", "softwaredefinednetworking", "cloudinfrastructuremanagement",
    "containerizedcloudservices", "cloudworkflowautomation", "datatransferoptimization", "cloudloggingmanagement", "datacenterprovisioning",
    "networktopology", "workloadautomationplatform", "scalingautomation", "publicclouddata", "distributeddatabase", "backupcloudsolution",
    "dataaccesslayer", "multiapplicationcloud", "loadbalancingdeployment", "elasticcloudscaling", "containerizedinfrastructure",
    "vm", "paaS", "IaC", "K8s", "CI/CD", "SaaS", "IaaS", "vpc", "cd", "cloud9", "rds", "vdi", "ecs", "dbaas", "edc", 
    "api", "sdk", "lambda", "cf", "ssl", "http", "https", "cdn", "cdn", "http2", "pki", "vpn", "api", "ipv6", "dns", 
    "ftps", "ssh", "s3", "efs", "db", "boto", "helm", "aci", "aws", "gcp", "azure", "cpu", "ram", "vps", "caaS", "edgex", 
    "sdn", "lfs", "cli", "appsvc", "ops", "e2e", "mvc", "uai", "devops", "mfa", "ssl", "tls", "api", "dbaas", "dmz", "hpc", 
    "tcp", "http2", "ftp", "dpdk", "siem", "vpn", "infra", "git", "json", "yaml", "toml", "stack", "cloud", "vms", "sfs", 
    "k8sc", "pkg", "lim", "os", "ts", "cloudlets", "mdm", "rbac", "lxd", "hpa", "csi", "paas", "e2e", "hvm", "js", "apigw", 
    "pkg", "nginx", "sftp", "vswitch", "tpm", "k8sd", "cf", "scm", "mfa", "acl", "osgi", "keymgmt", "sso", "cbt", "nat", 
    "snmp", "vpn", "antivirus", "fw", "nsx", "libvirt", "poc", "exec", "mmc", "pwa", "bastion", "kvs", "dcs", "ngfw",
    "edgeworkload", "cloudinfrastructurearchitecture", "cloudsql"
]
liste = list(dict.fromkeys(cloud_computing_terms))
with open('liste.txt', 'w', encoding='utf-8') as file:
    file.write(str(liste))