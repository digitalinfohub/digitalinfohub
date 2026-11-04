# Content data for the Tech Topic guide pages (part 2).

TOPICS = [
    {
        "slug": "cybersecurity",
        "name": "Cybersecurity",
        "short": "Security",
        "icon": "🛡️",
        "category": "Security",
        "title": "Cybersecurity Basics: Threats, Defences and Habits",
        "meta": "A practical guide to cybersecurity: the threats that matter most, the controls that actually reduce risk, and a checklist for protecting accounts, devices and data.",
        "lede": "Cybersecurity is the work of keeping systems, data and people safe from digital attack, and of recovering quickly when something goes wrong anyway.",
        "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Computer_security",
        "keywords": ["cybersecurity", "online security", "phishing", "multi-factor authentication", "ransomware", "security best practices"],
        "intro": [
            "Security is not a product you install once. It is a set of trade-offs between convenience, cost and risk, applied continuously. Every control you add has a usability price, and every control you skip is a bet that nobody will notice.",
            "Most incidents are not sophisticated. They begin with a reused password, a convincing email, an unpatched server or a backup that was never tested. Getting the basics right defeats the majority of attacks.",
        ],
        "sections": [
            {
                "id": "threats",
                "h": "The threats that actually matter",
                "p": [
                    "Phishing and social engineering remain the most common entry point because they target people rather than software. Ransomware turns a foothold into an operational emergency by encrypting data and demanding payment, and it increasingly steals data first so that backups alone are not enough.",
                    "Credential stuffing reuses passwords leaked from other sites. Supply-chain attacks compromise a trusted vendor or package so malicious code arrives inside something you already allow. Insider mistakes, exposed cloud storage and unpatched internet-facing services round out the list.",
                ],
            },
            {
                "id": "core-controls",
                "h": "The controls that reduce the most risk",
                "p": [
                    "Identity comes first. Multi-factor authentication, ideally with passkeys or hardware keys rather than SMS codes, blocks most account takeover. Password managers remove the incentive to reuse credentials and make long unique passwords practical.",
                    "Next comes recovery. Backups should be automatic, encrypted, stored separately from the main network, and restored in a test at least once a year. A backup you have never restored is a hope, not a plan.",
                ],
                "list": [
                    "Enable multi-factor authentication on email, banking and work accounts first.",
                    "Patch operating systems, browsers and internet-facing services quickly.",
                    "Use a password manager with unique credentials for every site.",
                    "Keep offline or immutable backups and test restoration.",
                    "Apply least privilege: nobody needs admin rights for daily work.",
                    "Log and alert on unusual sign-ins and privilege changes.",
                ],
            },
            {
                "id": "personal-checklist",
                "h": "A five-minute personal checklist",
                "p": [
                    "Secure your email account before anything else, because it is the reset path for everything you own. Then turn on automatic updates, check which third-party apps have access to your accounts, and remove the ones you no longer use.",
                    "On public networks, assume traffic can be observed and prefer your mobile connection for sensitive work. Treat urgency as a warning sign: real organisations do not ask for gift cards, passwords or one-time codes.",
                ],
                "callout": "If a message pressures you to act immediately, that pressure is the attack. Slow down and verify through a channel you chose.",
            },
            {
                "id": "business",
                "h": "What businesses should have in place",
                "p": [
                    "Beyond the basics, organisations need an inventory of assets, an owner for security decisions, a tested incident response plan and a way to report problems without fear. Regulatory duties around breach notification and data protection apply in most jurisdictions.",
                    "Security awareness training helps most when it is short, regular and tied to real examples from the organisation, not an annual slideshow that everyone clicks through.",
                ],
            },
        ],
        "facts": [
            "Phishing and stolen credentials cause more breaches than technical exploits.",
            "Multi-factor authentication is the highest-value single control for most people.",
            "Ransomware crews now steal data before encrypting it.",
            "An untested backup is not a recovery plan.",
        ],
        "faq": [
            {
                "q": "How often should I change my passwords?",
                "a": "Modern guidance favours long, unique passwords with multi-factor authentication over forced regular rotation. Change a password immediately when a service reports a breach or you suspect compromise.",
            },
            {
                "q": "Is antivirus enough?",
                "a": "No. It catches known malware but not a convincing phishing page, a stolen session cookie or a misconfiguration. It is one layer among several.",
            },
            {
                "q": "What should I do first after a breach?",
                "a": "Contain the damage: change the password from a clean device, revoke active sessions, enable multi-factor authentication and check for forwarding rules or new payment details added by the attacker.",
            },
        ],
        "related": ["zerotrustsecurity", "blockchain", "cloudcomputing"],
    },
    {
        "slug": "zerotrustsecurity",
        "name": "Zero Trust Security",
        "short": "Zero Trust",
        "icon": "🔒",
        "category": "Security",
        "title": "Zero Trust Security: Never Trust, Always Verify",
        "meta": "How zero trust replaces the network perimeter with continuous verification of identity, devices, apps and data, and how to adopt it without breaking your team.",
        "lede": "Zero trust is a security model that stops assuming anything inside the network is safe and verifies every request on its merits.",
        "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Zero_trust_security_model",
        "keywords": ["zero trust", "zero trust security", "least privilege", "microsegmentation", "identity security", "zero trust architecture"],
        "intro": [
            "Traditional security assumed a wall: trusted inside, untrusted outside. Remote work, cloud services and mobile devices dissolved that wall, so an attacker who steals one credential can often move anywhere.",
            "Zero trust starts from the opposite assumption: the network is already hostile and a breach is possible. Access is granted per request, based on who you are, what device you use, what you are asking for, and how risky the context looks.",
        ],
        "sections": [
            {
                "id": "principles",
                "h": "The principles behind it",
                "p": [
                    "Verify explicitly: authenticate and authorise using every available signal rather than trusting an IP address. Apply least privilege so a stolen account can reach as little as possible. Assume breach, and design so that one compromised component does not expose everything.",
                    "In practice these principles turn into identity-aware access, device posture checks, segmentation between workloads, encryption everywhere and detailed logging of who accessed what.",
                ],
                "list": [
                    "Identity: strong authentication, short-lived sessions, conditional access.",
                    "Devices: health and compliance checks before access is granted.",
                    "Network: microsegmentation between services, not one flat internal network.",
                    "Applications: per-app authorisation and secure direct access.",
                    "Data: classification, encryption and monitoring of unusual access.",
                ],
            },
            {
                "id": "implementation",
                "h": "How to adopt zero trust in stages",
                "p": [
                    "Start with identity and the highest-value applications. Put multi-factor authentication and single sign-on in front of them, remove standing admin rights, and route access through an identity-aware proxy instead of a flat VPN.",
                    "Then segment. Separate production from development, finance from engineering, and workloads from each other. Add continuous monitoring so you can see which rules are doing real work and which are legacy assumptions.",
                ],
                "callout": "Zero trust is a maturity journey, not a product you buy. The first milestone is knowing exactly who can reach your most sensitive system.",
            },
            {
                "id": "pitfalls",
                "h": "Where zero trust projects go wrong",
                "p": [
                    "The common failure is treating it as a vendor purchase. Tools enforce policy, but someone must decide what the policy should be and who owns it. Without that, teams end up with more agents and the same permissive habits.",
                    "The second failure is breaking workflows. If security makes legitimate work slower, people route around it. Pilot on one team, measure friction, and automate the approval paths that would otherwise become helpdesk tickets.",
                ],
            },
            {
                "id": "who-needs-it",
                "h": "Who needs it, and who can wait",
                "p": [
                    "Any organisation with remote staff, cloud workloads, contractors or valuable data benefits. Small teams can adopt the core of it cheaply by centralising identity, enforcing multi-factor authentication and using an identity-aware access proxy.",
                    "A solo user does not need a formal programme, but the same habits apply: unique credentials, device locks, minimal app permissions and review of what has access to your accounts.",
                ],
            },
        ],
        "facts": [
            "Zero trust removes implicit trust based on network location.",
            "Identity is the primary control plane in a zero trust design.",
            "Microsegmentation limits how far an attacker can move after a breach.",
            "It is a programme of incremental changes, not a single product.",
        ],
        "faq": [
            {
                "q": "Does zero trust mean no VPN?",
                "a": "Often it replaces a traditional VPN with identity-aware access that grants per-application access instead of broad network access, but many organisations run both during the transition.",
            },
            {
                "q": "Is zero trust only for large enterprises?",
                "a": "No. The core practices, strong identity, least privilege and segmentation, scale down to small teams and are often cheaper than recovering from an incident.",
            },
            {
                "q": "How long does adoption take?",
                "a": "A first meaningful milestone can take weeks for one critical application. A full programme across a complex estate is a multi-year effort measured in reduced standing access and faster incident containment.",
            },
        ],
        "related": ["cybersecurity", "cloudcomputing", "internetofthings"],
    },
    {
        "slug": "internetofthings",
        "name": "Internet of Things",
        "short": "IoT",
        "icon": "📡",
        "category": "Infrastructure",
        "title": "Internet of Things Explained: Sensors and Risk",
        "meta": "What the Internet of Things is, how connected devices actually work, where IoT delivers value, and the security and privacy questions every deployment has to answer.",
        "lede": "The Internet of Things is what happens when everyday objects get sensors, connectivity and software, so they can report on the physical world and act on it.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Internet_of_things",
        "keywords": ["internet of things", "IoT explained", "IoT security", "smart home", "industrial IoT", "sensors"],
        "intro": [
            "A thermostat that reports temperature to an app is IoT. So is a factory sensor that predicts a bearing failure, a soil probe that triggers irrigation, and a fleet tracker that reroutes around traffic.",
            "The category is defined by a pattern rather than a device: physical measurement, a network connection, and software that turns readings into action.",
        ],
        "sections": [
            {
                "id": "architecture",
                "h": "How an IoT system is put together",
                "p": [
                    "Devices contain sensors, a small processor and a radio. They usually talk to a gateway that bridges short-range protocols to the internet, and data lands in a cloud platform that stores it, applies rules and exposes it to dashboards or other systems.",
                    "Edge processing is increasingly common, because sending every raw reading to the cloud is expensive and slow. Filtering or aggregating at the gateway cuts bandwidth and lets a device react in milliseconds without a round trip.",
                ],
                "list": [
                    "Device: sensors, actuators, firmware and limited compute.",
                    "Connectivity: Wi-Fi, cellular, Bluetooth, LoRaWAN or wired fieldbus.",
                    "Gateway: protocol translation, buffering, local rules and updates.",
                    "Platform: ingestion, storage, analytics, alerts and device management.",
                    "Application: dashboards, automation and integration with business systems.",
                ],
            },
            {
                "id": "uses",
                "h": "Where IoT earns its cost",
                "p": [
                    "Industrial monitoring reduces unplanned downtime by catching vibration or temperature changes early. Utilities use smart meters to balance load. Logistics tracks assets and conditions such as temperature for cold-chain compliance. Buildings tune heating and lighting to occupancy.",
                    "Consumer IoT is the most visible segment, but the strongest business cases are usually unglamorous: a sensor that prevents one costly failure can pay for an entire deployment.",
                ],
            },
            {
                "id": "security",
                "h": "Security, privacy and long-term maintenance",
                "p": [
                    "Connected devices are hard to secure because they are numerous, cheap, long-lived and often shipped with default passwords. Botnets built from poorly secured cameras and routers still cause some of the largest denial-of-service attacks on record.",
                    "Buy devices that publish firmware update support and change the default password immediately. On the network, put IoT on a separate segment so a compromised device cannot reach laptops or servers.",
                ],
                "callout": "Ask one question before buying any connected device: how long will it receive security updates, and who is responsible for installing them?",
            },
            {
                "id": "starting",
                "h": "Starting a sensible IoT project",
                "p": [
                    "Pick one measurement that changes a decision, instrument it properly, and prove the value before scaling. Calibration and data quality decide whether the readings are trustworthy, and connectivity decisions dictate battery life and cost for years.",
                    "Plan for failure: devices lose connectivity, batteries die and clocks drift. Systems that buffer locally and reconcile later survive real deployments better than designs that assume a perfect network.",
                ],
            },
        ],
        "facts": [
            "IoT is a pattern: sense, connect, decide, act.",
            "Edge processing reduces bandwidth and latency for high-frequency data.",
            "Default credentials on connected devices remain a major attack path.",
            "Battery life and update support shape device choices more than raw specs.",
        ],
        "faq": [
            {
                "q": "Is a smart speaker an IoT device?",
                "a": "Yes. It contains microphones and software, connects to cloud services and acts on voice input, which fits the definition even though it is marketed as a consumer product.",
            },
            {
                "q": "What is the difference between IoT and industrial IoT?",
                "a": "Industrial IoT applies the same pattern to machines and infrastructure where reliability, determinism and safety standards are far stricter than in a home.",
            },
            {
                "q": "How do I secure a home full of connected devices?",
                "a": "Change default passwords, enable automatic updates, place devices on a guest or separate network, disable features you do not use, and replace hardware that no longer receives patches.",
            },
        ],
        "related": ["edgecomputing", "5gnetworks", "digitaltwins"],
    },
    {
        "slug": "5gnetworks",
        "name": "5G Networks",
        "short": "5G",
        "icon": "📶",
        "category": "Infrastructure",
        "title": "5G Networks Explained: Speed, Latency and Limits",
        "meta": "What 5G actually changes: faster data, lower latency and far more connected devices, plus the coverage, cost and spectrum realities behind the marketing.",
        "lede": "5G is the fifth generation of mobile networking, designed for faster data, quicker responses and a far denser set of connected devices than 4G could support.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/5G",
        "keywords": ["5G", "5G networks", "what is 5G", "5G vs 4G", "network latency", "private 5G"],
        "intro": [
            "Every mobile generation changes what a network is optimised for. 5G is built around three goals: enhanced mobile broadband, ultra-reliable low-latency communication, and massive machine-type communication.",
            "Those goals are met to different degrees in different places. A 5G icon on a phone does not guarantee a dramatic improvement, because real performance depends on spectrum, density of cells and whether the operator has deployed the standalone core.",
        ],
        "sections": [
            {
                "id": "whats-different",
                "h": "What is genuinely different",
                "p": [
                    "5G uses wider channels and more efficient radio coding, so peak speeds and capacity rise substantially. It also supports many more devices per square kilometre, which matters for sensors and industrial equipment rather than phones.",
                    "Latency can drop to single-digit milliseconds on well-built networks, and network slicing lets an operator carve dedicated performance guarantees for a specific customer or application.",
                ],
                "list": [
                    "Higher throughput, especially on millimetre-wave spectrum.",
                    "Lower latency for time-sensitive applications.",
                    "Higher device density per cell.",
                    "Network slicing for dedicated virtual networks.",
                    "Standalone core for services that do not depend on 4G.",
                ],
            },
            {
                "id": "spectrum",
                "h": "Spectrum decides the experience",
                "p": [
                    "Low-band spectrum travels far and penetrates buildings but offers modest speed. Mid-band balances coverage and capacity and carries most real-world 5G traffic. Millimetre-wave delivers very high speed over short distances and is easily blocked by walls and even foliage.",
                    "That physics explains why coverage maps look optimistic. A site may have mid-band capacity in a city centre and fall back to 4G a few streets away.",
                ],
            },
            {
                "id": "uses",
                "h": "Where 5G changes outcomes",
                "p": [
                    "Fixed wireless access brings broadband to premises without fibre. Private 5G gives factories, ports and mines dedicated coverage with predictable performance. Live broadcast, remote inspection and connected vehicles benefit from low latency.",
                    "For ordinary phone users the improvement is often incremental, because 4G is already adequate for messaging, maps and video. The bigger shift is in machines and infrastructure.",
                ],
                "callout": "5G is less about your phone being faster and more about machines being connected reliably.",
            },
            {
                "id": "reality-check",
                "h": "The reality check",
                "p": [
                    "Dense deployment means more cells, more fibre backhaul and more power, which makes 5G expensive to build. Coverage indoors and in rural areas lags urban rollout, and some promised features depend on a standalone core that operators are still deploying.",
                    "Private networks solve this for organisations willing to fund their own coverage. For everyone else, the practical advice is simple: judge the connection you actually get where you work, not the peak figure in an advertisement.",
                ],
            },
        ],
        "facts": [
            "5G's headline benefits are speed, latency and device density.",
            "Mid-band spectrum carries most usable 5G capacity.",
            "Millimetre-wave is fast but short-range and easily blocked.",
            "Private 5G is often more transformative than public consumer coverage.",
        ],
        "faq": [
            {
                "q": "Is 5G faster than 4G?",
                "a": "Yes in capacity and peak speed, but the everyday difference depends on spectrum, signal quality and network load. Congested coverage can feel similar to good 4G.",
            },
            {
                "q": "What is standalone 5G?",
                "a": "A 5G core network that does not rely on 4G infrastructure for control. It enables slicing and very low latency, and requires a separate deployment by the operator.",
            },
            {
                "q": "Does 5G cause health problems?",
                "a": "Radio-frequency exposure limits are set by international bodies and public networks operate within them. Reviews by major health agencies have not established a causal link at those exposure levels.",
            },
        ],
        "related": ["internetofthings", "edgecomputing", "virtualreality"],
    },
    {
        "slug": "edgecomputing",
        "name": "Edge Computing",
        "short": "Edge",
        "icon": "📍",
        "category": "Infrastructure",
        "title": "Edge Computing Explained: Processing Near the Data",
        "meta": "Why edge computing moves processing closer to users and devices, how it differs from cloud, which workloads benefit, and the operational trade-offs to plan for.",
        "lede": "Edge computing puts computation near the place where data is created, so a decision can be made in milliseconds instead of travelling to a distant data centre.",
        "image": "https://images.unsplash.com/photo-1727434032773-af3cd98375ba?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Edge_computing",
        "keywords": ["edge computing", "what is edge computing", "edge vs cloud", "latency", "distributed computing", "edge AI"],
        "intro": [
            "Cloud computing centralised processing in large data centres. Edge computing pushes some of that work back out towards cameras, vehicles, factory floors, retail stores and cell towers.",
            "It is not a replacement for the cloud. It is a complement: local processing for what must be immediate, cloud processing for everything that benefits from scale, history and coordination.",
        ],
        "sections": [
            {
                "id": "why",
                "h": "Why move compute to the edge",
                "p": [
                    "Physics sets a floor on latency. A round trip to a distant region costs tens to hundreds of milliseconds, which is fine for loading a page and unacceptable for a braking decision or an industrial safety interlock.",
                    "Bandwidth and cost matter too. Sending every frame from a hundred cameras to the cloud is expensive and often pointless when only a few seconds contain an event. Filtering locally sends the signal and drops the noise.",
                ],
                "list": [
                    "Latency: react within milliseconds without a round trip.",
                    "Bandwidth: upload summaries instead of raw streams.",
                    "Resilience: keep working when the backhaul fails.",
                    "Privacy: keep sensitive footage or readings on site.",
                    "Cost: reduce cloud egress and storage charges.",
                ],
            },
            {
                "id": "architecture",
                "h": "What an edge deployment looks like",
                "p": [
                    "Edge sits on a spectrum. Device edge runs directly on sensors and cameras. Near edge uses a local server or gateway in a store, factory or cell site. Regional edge places small data centres closer to users than a central region.",
                    "Workloads are usually containerised so the same application can run in several locations. Management, updates and observability are centralised, because hundreds of remote sites cannot be visited by hand.",
                ],
            },
            {
                "id": "tradeoffs",
                "h": "The trade-offs nobody mentions in the keynote",
                "p": [
                    "Distributed systems are harder than centralised ones. Every edge site needs power, cooling, physical security and a plan for when it fails. Software must tolerate intermittent connectivity and partial data.",
                    "Edge hardware is heterogeneous and often unpatched. Model and application updates must be signed and roll back safely, and someone has to own the fleet after the pilot ends.",
                ],
                "callout": "If the cloud round trip is fast enough for your use case, the cloud is almost always the simpler and cheaper answer.",
            },
            {
                "id": "uses",
                "h": "Where edge computing fits best",
                "p": [
                    "Computer vision on production lines, autonomous vehicles, retail analytics, medical devices, content delivery and 5G-enabled industrial control all justify local processing. Each combines a hard latency or bandwidth constraint with a clear cost of failure.",
                    "A useful test is to measure the real latency requirement first. If the answer is hundreds of milliseconds, a well-designed cloud service will usually do the job.",
                ],
            },
        ],
        "facts": [
            "Edge reduces latency by shortening the distance data travels.",
            "Edge and cloud are complementary layers, not competitors.",
            "Remote sites need power, cooling, security and update plans.",
            "Only workloads with a hard latency or bandwidth constraint justify the complexity.",
        ],
        "faq": [
            {
                "q": "Is edge computing the same as a content delivery network?",
                "a": "A CDN is one form of edge computing focused on caching content close to users. Edge computing is broader and includes running application logic and analytics locally.",
            },
            {
                "q": "Does edge computing replace the cloud?",
                "a": "No. Edge handles local, time-sensitive work while the cloud provides central storage, coordination, training and long-term analytics.",
            },
            {
                "q": "What is edge AI?",
                "a": "Running machine learning models on or near the device rather than in a data centre, usually with smaller optimised models so inference can happen locally.",
            },
        ],
        "related": ["internetofthings", "serverlesscomputing", "cloudcomputing"],
    },
    {
        "slug": "serverlesscomputing",
        "name": "Serverless Computing",
        "short": "Serverless",
        "icon": "⚡",
        "category": "Infrastructure",
        "title": "Serverless Computing Explained: Trade-offs",
        "meta": "How serverless computing works, when per-request functions beat always-on servers, and the cold-start, lock-in and observability trade-offs to weigh up.",
        "lede": "Serverless computing lets you deploy code or managed services without choosing, patching or scaling a server yourself.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Serverless_computing",
        "keywords": ["serverless", "serverless computing", "functions as a service", "FaaS", "cloud functions", "cold start"],
        "intro": [
            "The name is misleading: servers still exist, you just do not manage them. The provider runs your code in response to an event, scales it automatically and bills for the compute time you actually use.",
            "That changes the economics for spiky or unpredictable workloads. It also changes the engineering, because a function is short-lived, stateless and constrained by the platform's limits.",
        ],
        "sections": [
            {
                "id": "models",
                "h": "Functions and managed backends",
                "p": [
                    "Functions as a service runs a handler when an HTTP request, queue message, file upload or schedule fires. Managed services extend the idea to databases, queues, authentication and storage, so a small team can run a real product without operating infrastructure.",
                    "The practical pattern is composition: a function handles one small piece, an event bus connects it to the next, and managed services hold state. Applications are built from many small units rather than one large server.",
                ],
                "list": [
                    "Event sources: HTTP, queues, schedules, object storage, database changes.",
                    "Compute: short-lived stateless functions with a maximum runtime.",
                    "State: managed databases, object storage and key-value stores.",
                    "Integration: event buses and workflow orchestration services.",
                    "Delivery: edge functions for low-latency personalisation and routing.",
                ],
            },
            {
                "id": "benefits",
                "h": "Why teams choose it",
                "p": [
                    "Scaling is automatic, including scaling to zero, so a side project costs almost nothing when idle. There are no servers to patch and no capacity planning, which lets a small team ship quickly.",
                    "Because functions are small and event-driven, deployments are usually faster and blast radius is smaller. That makes serverless a good fit for APIs with uneven traffic, webhooks, image processing and scheduled jobs.",
                ],
            },
            {
                "id": "tradeoffs",
                "h": "The trade-offs to plan for",
                "p": [
                    "Cold starts add latency when a function has not run recently, though provisioned concurrency and faster runtimes reduce this. Long-running or steady high-volume workloads are often cheaper on containers.",
                    "Per-function observability is harder than watching one server, so tracing and structured logging are mandatory rather than optional. Deep use of provider-specific services also raises the cost of moving later.",
                ],
                "callout": "Serverless is a poor fit for anything that needs a persistent local process, large in-memory state or predictable long-running compute.",
            },
            {
                "id": "when",
                "h": "When to use it, and when not to",
                "p": [
                    "Choose serverless for event-driven APIs, glue between services, scheduled tasks, media pipelines, authentication hooks and prototypes where speed to launch matters more than unit cost.",
                    "Choose containers or virtual machines for steady high throughput, long-lived connections, custom runtimes or strict latency requirements. Many teams run both, using serverless for the edges and containers for the core.",
                ],
            },
        ],
        "facts": [
            "Billing is per request and compute time, not per idle server.",
            "Functions are stateless, so state must live in a separate service.",
            "Cold starts affect latency after periods of inactivity.",
            "Serverless is strongest for spiky, event-driven workloads.",
        ],
        "faq": [
            {
                "q": "Is serverless cheaper than running servers?",
                "a": "It is cheaper when traffic is low or spiky because you pay only for execution. At sustained high utilisation, reserved containers or servers are usually less expensive per request.",
            },
            {
                "q": "What is a cold start?",
                "a": "The extra latency when a platform must initialise a new execution environment before running your function, typically after idle time or a scale-up event.",
            },
            {
                "q": "Can serverless applications use a database?",
                "a": "Yes, but connection handling needs care because each function instance may open its own connection. Pooling services and HTTP-based database drivers solve most of the problem.",
            },
        ],
        "related": ["cloudcomputing", "devops", "apis"],
    },
]
