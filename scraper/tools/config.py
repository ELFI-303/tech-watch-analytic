import os

categories = {
    "Programming and Development": [
        "software development", "programming", "coding", "scripting",
        "algorithm", "data structure", "backend", "frontend",
        "API", "microservices", "containerization", "cloud-native", "k8s", "kubernetes"
    ],
    "Emerging Technologies": [
        "artificial intelligence", "machine learning", "deep learning",
        "big data", "data-driven", "blockchain", "decentralized",
        "edge computing", "serverless", "IoT", "ai", "ia"
    ],
    "Cloud and Infrastructure": [
        "cloud computing", "AWS", "Azure", "Google Cloud", "Kubernetes",
        "virtualization", "infrastructure as code", "DevOps",
        "continuous integration", "continuous delivery", "CI/CD", "ci", "cd",
        "scalability", "resiliency"
    ],
    "Software Architecture and Practices": [
        "design patterns", "agile development", "scrum", "kanban",
        "code review", "refactoring", "technical debt",
        "performance optimization", "test automation", "unit testing", "solid"
    ],
    "Security and Compliance": [
        "cybersecurity", "data privacy", "encryption", "authentication",
        "authorization", "vulnerability management", "zero trust",
        "compliance", "GDPR", "SOC", "owasp", "malware"
    ],
    "Data and Analytics": [
        "data pipeline", "ETL", "data visualization", "business intelligence",
        "analytics", "data lake", "data warehouse", "real-time processing",
        "predictive analytics"
    ],
    "Career and Trends": [
        "emerging technologies", "industry trends", "tech forecast",
        "developer tools", "open source", "productivity tools",
        "programming languages", "software engineering practices"
    ],
    "Other Topics": [
        "performance tuning", "debugging", "version control", "git",
        "collaboration tools", "developer productivity", "software testing",
        "IT infrastructure", "automation", "distributed systems"
    ]
}

azureTechBlogs = [
    "https://techcommunity.microsoft.com/category/Azure/blog/AppsonAzureBlog",
    "https://techcommunity.microsoft.com/category/Azure/blog/AzureHighPerformanceComputingBlog",
    "https://techcommunity.microsoft.com/category/cis/blog/CoreInfrastructureandSecurityBlog",
    "https://techcommunity.microsoft.com/category/azure-network-security/blog/AzureNetworkSecurityBlog",
    "https://techcommunity.microsoft.com/category/AzureDatabases/blog/AzureSynapseAnalyticsBlog",
    "https://techcommunity.microsoft.com/category/AI/blog/Azure-AI-Services-blog",
    "https://techcommunity.microsoft.com/category/Azure/blog/AzureMigrationBlog",
    "https://techcommunity.microsoft.com/category/azure/blog/azurearchitectureblog",
    "https://techcommunity.microsoft.com/category/azure/blog/azuregovernanceandmanagementblog",
    "https://techcommunity.microsoft.com/category/azure/blog/azureinfrastructureblog",
    "https://techcommunity.microsoft.com/category/azure/blog/integrationsonazureblog",
    "https://techcommunity.microsoft.com/category/azure/blog/azurecompute",
    "https://techcommunity.microsoft.com/category/azure/blog/azurestorageblog",
    "https://techcommunity.microsoft.com/category/azure/blog/azurenetworkingblog",
]

googleIgnore = [
    'https://cloud.google.com/blog/topics/training-certifications/',
    'https://cloud.google.com/blog/topics/supply-chain-logistics/',
    'https://cloud.google.com/blog/topics/retail/',
    'https://cloud.google.com/blog/products/gaming/',
    'https://cloud.google.com/blog/topics/manufacturing/',
    'https://cloud.google.com/blog/topics/sustainability/',
    'https://cloud.google.com/blog/topics/healthcare-life-sciences/',
    'https://cloud.google.com/blog/topics/financial-services/',
    'https://cloud.google.com/blog/topics/public-sector/',
    'https://cloud.google.com/blog/topics/startups/',
    'https://cloud.google.com/blog/products/media-entertainment/',
    'https://cloud.google.com/blog/products/sap-google-cloud/',
    'https://cloud.google.com/blog/topics/consumer-packaged-goods/',
    'https://cloud.google.com/blog/topics/inside-google-cloud/',
    'https://cloud.google.com/blog/products/maps-platform/',
    'https://cloud.google.com/blog/products/productivity-collaboration/',
    'https://cloud.google.com/blog/products/spanner/',
    'https://cloud.google.com/blog/topics/consulting/',
    'https://cloud.google.com/blog/topics/customers/',
    'https://cloud.google.com/blog/products/chrome-enterprise/',
    'https://cloud.google.com/blog/products/business-intelligence/',
    'https://cloud.google.com/blog/topics/developers-practitioners/',
    'https://cloud.google.com/blog/ko/products/'
]

ollama_url = os.environ.get('OLLAMA_BASE_URL')