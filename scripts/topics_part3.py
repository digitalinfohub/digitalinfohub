# Content data for the Tech Topic guide pages (part 3).

TOPICS = [
    {
        "slug": "devops",
        "name": "DevOps",
        "short": "DevOps",
        "icon": "⚙️",
        "category": "Engineering",
        "title": "DevOps Explained: CI/CD, Automation and Culture",
        "meta": "How DevOps connects development and operations through automation, CI/CD pipelines, infrastructure as code and measurement, and the habits that make it stick.",
        "lede": "DevOps is a way of working that makes one team responsible for software from first commit to running in production.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/DevOps",
        "keywords": ["DevOps", "what is DevOps", "CI/CD", "infrastructure as code", "deployment pipeline", "observability"],
        "intro": [
            "When development and operations sit in separate silos, developers are rewarded for shipping features and operations for stability, and the two goals collide at every release. DevOps removes the handoff by making the same team own the outcome.",
            "The visible part is tooling: pipelines, automation and dashboards. The part that decides whether it works is culture, because automation only helps if people trust it enough to use it.",
        ],
        "sections": [
            {
                "id": "practices",
                "h": "The core practices",
                "p": [
                    "Continuous integration merges small changes frequently and tests each one automatically. Continuous delivery keeps the software always releasable, with deployment to production a routine, low-drama action rather than an event.",
                    "Infrastructure as code describes servers, networks and permissions in version-controlled files, so environments can be recreated exactly. Observability, meaning logs, metrics and traces tied to user experience, closes the loop by showing what actually happens after a deploy.",
                ],
                "list": [
                    "Small, frequent changes instead of large batch releases.",
                    "Automated tests that run on every pull request.",
                    "Infrastructure defined in code and reviewed like code.",
                    "Immutable deployments and one-step rollback.",
                    "Metrics, logs and traces with alerts tied to user impact.",
                    "Blameless reviews after incidents that change the system, not the person.",
                ],
            },
            {
                "id": "pipeline",
                "h": "What a healthy pipeline looks like",
                "p": [
                    "A commit triggers linting, tests, a build and a security check. Artefacts are versioned and signed. Deployment to staging is automatic, promotion to production is a deliberate step, and rollback is a single command that has been rehearsed.",
                    "Speed matters because a slow pipeline invites bypassing. If feedback takes an hour, developers batch changes, and large batches are exactly what causes risky releases.",
                ],
            },
            {
                "id": "measuring",
                "h": "How to measure progress",
                "p": [
                    "Four measures cover most of the ground: deployment frequency, lead time from commit to production, change failure rate, and time to restore service. They balance speed against stability so a team cannot game one at the expense of the other.",
                    "Track them as trends, not targets. Turning a metric into a quota produces the behaviour the quota rewards, which is rarely the behaviour you wanted.",
                ],
                "callout": "The goal is not to deploy more often. It is to make deploying boring, so that changes are small and recovery is fast.",
            },
            {
                "id": "getting-started",
                "h": "Getting started without a platform team",
                "p": [
                    "Start with version control, a CI service that runs tests, and one repeatable deployment script. Then add automated environment creation, and only afterwards consider orchestration platforms.",
                    "Write down what runs where and who can change it. Most DevOps pain comes from undocumented environments and permissions that nobody dares touch.",
                ],
            },
        ],
        "facts": [
            "DevOps is a cultural and organisational change supported by tooling.",
            "Small, frequent releases are safer than large, rare ones.",
            "Infrastructure as code makes environments reproducible and reviewable.",
            "Deployment frequency and change failure rate should improve together.",
        ],
        "faq": [
            {
                "q": "Is DevOps just a job title?",
                "a": "It is a way of working, though many organisations hire platform or DevOps engineers to build the shared tooling. A single person cannot own a culture on their own.",
            },
            {
                "q": "Do I need Kubernetes for DevOps?",
                "a": "No. Version control, automated tests, reproducible infrastructure and fast rollback deliver most of the benefit without any orchestrator.",
            },
            {
                "q": "What is the difference between CI and CD?",
                "a": "Continuous integration automatically tests every change. Continuous delivery keeps the product deployable at any time, while continuous deployment goes further and releases automatically.",
            },
        ],
        "related": ["serverlesscomputing", "opensource", "cloudcomputing"],
    },
    {
        "slug": "apis",
        "name": "APIs",
        "short": "APIs",
        "icon": "🔌",
        "category": "Engineering",
        "title": "APIs Explained: REST, GraphQL and Good Design",
        "meta": "What an API is, how REST, GraphQL and gRPC differ, how authentication and versioning work, and the design choices that keep integrations from breaking.",
        "lede": "An API is a contract that lets one piece of software ask another for data or an action without knowing how the other is built.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/API",
        "keywords": ["API", "what is an API", "REST API", "GraphQL", "gRPC", "API authentication"],
        "intro": [
            "Every app that shows a map, takes a payment or sends a message is calling an API. The interface hides implementation details, so the provider can change internals without breaking every client.",
            "Good APIs are predictable. Names, error formats and pagination behave the same way everywhere, and a developer can guess the right call after reading one example.",
        ],
        "sections": [
            {
                "id": "styles",
                "h": "REST, GraphQL and gRPC",
                "p": [
                    "REST models resources with HTTP verbs and URLs. It is simple, cacheable and universally understood, which is why it dominates public APIs. GraphQL exposes a typed schema and lets the client ask for exactly the fields it needs, which suits complex frontends with varied data requirements.",
                    "gRPC uses binary messages over HTTP/2 for fast, strongly typed service-to-service calls. It is common inside microservice architectures where performance and schema enforcement matter more than browser compatibility.",
                ],
                "list": [
                    "REST: resource-oriented, cache-friendly, easy to debug.",
                    "GraphQL: client-selected fields, one endpoint, strong typing.",
                    "gRPC: compact binary transport, streaming, internal services.",
                    "Webhooks: the provider calls you when something changes.",
                ],
            },
            {
                "id": "auth",
                "h": "Authentication and authorisation",
                "p": [
                    "Public APIs use keys to identify a project, OAuth for delegated access on a user's behalf, and short-lived tokens for sensitive operations. Keys must be treated as secrets and rotated when exposed.",
                    "Authorisation is separate from authentication. A valid token still needs a permission check on every action, and object-level checks must prevent one customer from reading another's data by changing an identifier.",
                ],
                "callout": "Never ship a secret API key in a mobile app or browser bundle. Anything the client can read, an attacker can read too.",
            },
            {
                "id": "design",
                "h": "Design rules worth following",
                "p": [
                    "Return consistent shapes, use clear status codes, and paginate everything that could grow. Rate-limit with informative headers, document errors with stable codes, and make idempotency explicit so a retried payment does not charge twice.",
                    "Version deliberately. Additive changes are usually safe, but removing or renaming a field breaks clients that you cannot see. Deprecation notices with a migration window are cheaper than an outage.",
                ],
                "list": [
                    "Use plural, predictable resource names.",
                    "Return errors with a stable code and a human-readable message.",
                    "Support pagination and filtering on every list endpoint.",
                    "Provide an idempotency key for unsafe retries.",
                    "Publish an OpenAPI or schema document and keep it current.",
                    "Log requests with correlation IDs for support and debugging.",
                ],
            },
            {
                "id": "consuming",
                "h": "Using someone else's API",
                "p": [
                    "Read the rate limits and error codes before writing code, and implement retries with exponential backoff plus jitter. Cache responses where the provider allows it, and design so that an unavailable third party degrades gracefully instead of taking your product down.",
                    "Check the provider's deprecation policy and status history. A service that changes behaviour without notice is a liability no matter how good the documentation looks.",
                ],
            },
        ],
        "facts": [
            "An API is a contract, so stability is a feature.",
            "REST dominates public APIs; gRPC dominates internal service calls.",
            "Client-side keys are public by definition and cannot hold secrets.",
            "Retries need idempotency or they duplicate side effects.",
        ],
        "faq": [
            {
                "q": "What does API stand for?",
                "a": "Application Programming Interface: a defined way for two programs to exchange requests and data without exposing their internal implementation.",
            },
            {
                "q": "Is GraphQL better than REST?",
                "a": "Neither is universally better. GraphQL reduces over-fetching for complex clients but adds caching, query-cost and tooling complexity. REST is simpler to cache and operate.",
            },
            {
                "q": "How do I keep an API key safe in a website?",
                "a": "Do not put it in the website. Route requests through your own backend or a serverless function that holds the key privately and applies its own access checks.",
            },
        ],
        "related": ["devops", "serverlesscomputing", "opensource"],
    },
    {
        "slug": "opensource",
        "name": "Open Source",
        "short": "Open Source",
        "icon": "🌐",
        "category": "Engineering",
        "title": "Open Source Explained: Licences, Contribution, Risk",
        "meta": "How open source software works, the difference between permissive and copyleft licences, how projects are sustained, and what to check before depending on one.",
        "lede": "Open source software is published with a licence that lets anyone use, study, modify and share it, which turned shared code into the foundation of the modern internet.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Open-source_software",
        "keywords": ["open source", "open source licences", "MIT licence", "GPL", "contributing to open source", "software supply chain"],
        "intro": [
            "Almost every product you use runs on open source: operating systems, web servers, programming languages, databases, browsers and build tools. The code is public, but that does not mean it is unowned or free of obligations.",
            "The licence is what makes a project open source. It grants permissions and sets conditions, and those conditions decide what you can do with the code in your own product.",
        ],
        "sections": [
            {
                "id": "licences",
                "h": "Licences, in plain language",
                "p": [
                    "Permissive licences such as MIT, Apache 2.0 and BSD let you use the code in commercial and closed products with few conditions, usually attribution and preservation of notices. Apache 2.0 adds an explicit patent grant.",
                    "Copyleft licences such as GPL require that derivative works distributed to others remain under the same licence, which can matter a great deal for a company shipping a proprietary product. Network copyleft licences extend the requirement to software offered as a service.",
                ],
                "list": [
                    "MIT and BSD: minimal conditions, maximum flexibility.",
                    "Apache 2.0: permissive with an explicit patent grant.",
                    "LGPL: copyleft on the library itself, with a linking allowance.",
                    "GPL: strong copyleft on distributed derivative works.",
                    "AGPL: copyleft triggered by network use as well as distribution.",
                ],
            },
            {
                "id": "communities",
                "h": "How projects are actually sustained",
                "p": [
                    "A healthy project has a clear governance model, a release process, responsive maintainers and documented contribution guidelines. Many critical libraries are maintained by a handful of people, sometimes unpaid, which is a real resilience risk for the industry.",
                    "Funding models include sponsorship, commercial support, hosted services and foundations. Projects backed by a foundation generally have clearer continuity than those tied to one company's roadmap.",
                ],
            },
            {
                "id": "contributing",
                "h": "Contributing without wasting anyone's time",
                "p": [
                    "Start by reading the contribution guide and searching existing issues. Reproduce the bug on the current version, describe expected and actual behaviour, and include a minimal test case.",
                    "Small, focused pull requests get reviewed. Large rewrites from strangers rarely do, because review cost falls on volunteers who owe you nothing. Documentation and tests are welcome contributions that also teach you the codebase.",
                ],
                "callout": "Before filing an issue, check whether it is a bug or a configuration problem. Maintainers are more responsive to people who did the first five minutes of diagnosis.",
            },
            {
                "id": "risk",
                "h": "Managing open source risk",
                "p": [
                    "Track your dependencies, because most of your code is written by people you have never met. Lock file versions, scan for known vulnerabilities, and have a plan for applying patches quickly.",
                    "Check licence compatibility before adopting a library, and consider the health of the project: recent releases, responsive maintainers and a history of handling security reports. Abandoned dependencies accumulate quietly until they become urgent.",
                ],
            },
        ],
        "facts": [
            "The licence, not the public repository, defines open source.",
            "Permissive licences allow closed products; copyleft licences impose sharing conditions.",
            "Many critical projects are maintained by very small teams.",
            "Dependency and licence audits belong in the build pipeline.",
        ],
        "faq": [
            {
                "q": "Does open source mean free of charge?",
                "a": "Usually the software is available at no cost, but the licence is about freedom to use and modify, not price. Support, hosted versions and enterprise features are often paid.",
            },
            {
                "q": "Can I use open source in a commercial product?",
                "a": "Generally yes, provided you follow the licence. Permissive licences are straightforward. Copyleft licences may require you to publish the modified source of distributed derivative works.",
            },
            {
                "q": "Is open source less secure?",
                "a": "Not inherently. Public code can be reviewed by anyone, which helps, but review only happens when people actually look. Dependency hygiene and prompt patching matter more than whether source is public.",
            },
        ],
        "related": ["devops", "artificialintelligence", "apis"],
    },
    {
        "slug": "semiconductors",
        "name": "Semiconductors",
        "short": "Chips",
        "icon": "💽",
        "category": "Hardware",
        "title": "Semiconductors Explained: How Chips Are Made",
        "meta": "How semiconductors work, why fabrication is so hard, what chip process nodes really mean, and why the supply chain is now a geopolitical issue.",
        "lede": "Semiconductors are materials that can switch between conducting and insulating, which makes them the physical foundation of every processor, sensor and radio on earth.",
        "image": "https://images.unsplash.com/photo-1727434032773-af3cd98375ba?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Semiconductor",
        "keywords": ["semiconductors", "how chips are made", "chip fabrication", "process node", "silicon", "semiconductor supply chain"],
        "intro": [
            "A transistor is a switch with no moving parts. Shrinking billions of them onto a sliver of silicon is what made computing cheap, and the manufacturing process required to do it is among the most complex engineering feats humans have achieved.",
            "Semiconductors sit at the intersection of physics, chemistry and logistics. That is why chip policy became industrial policy almost everywhere at once.",
        ],
        "sections": [
            {
                "id": "physics",
                "h": "What makes a semiconductor useful",
                "p": [
                    "Pure silicon is a poor conductor. Adding tiny amounts of other elements, called doping, gives it controlled regions of excess or deficit of electrons. Junctions between those regions form diodes and transistors that can amplify or switch signals.",
                    "Because the behaviour can be controlled precisely and patterned at microscopic scale, the same base material can implement logic, memory, power control, image sensing and radio communication.",
                ],
            },
            {
                "id": "fabrication",
                "h": "How a chip is fabricated",
                "p": [
                    "A silicon wafer is coated with light-sensitive material and exposed through a mask that carries the circuit pattern. Etching, deposition and doping build the structure layer by layer, often hundreds of steps over several months.",
                    "The most advanced logic needs extreme ultraviolet lithography, machines with elaborate optics and a supply chain of their own. Even a modest fab costs billions and needs ultra-pure water, gases and air handling.",
                ],
                "list": [
                    "Design: architecture, logic and verification, increasingly assisted by AI tools.",
                    "Wafer production: growing and polishing near-perfect silicon crystals.",
                    "Fabrication: lithography, etching, deposition and doping across hundreds of steps.",
                    "Packaging and test: cutting dies, connecting them and rejecting failures.",
                    "Integration: memory, power delivery and thermal design around the chip.",
                ],
            },
            {
                "id": "nodes",
                "h": "What process nodes mean now",
                "p": [
                    "A number like 3nm once described a physical feature. Today it is largely marketing shorthand for a generation of density and efficiency, and designs from different foundries are not directly comparable.",
                    "Advanced packaging now matters as much as shrinking transistors. Stacking chips and connecting them with high-bandwidth links lets designers build large systems without putting everything on one costly die.",
                ],
                "callout": "Performance per watt, not the node name, is the number that decides whether a chip is right for a device.",
            },
            {
                "id": "supply-chain",
                "h": "Why the supply chain is strategic",
                "p": [
                    "Design is concentrated in a few countries, advanced fabrication in very few, and packaging and assembly in others. A disruption anywhere in that chain can stop production worldwide, as recent shortages demonstrated across cars, appliances and consumer electronics.",
                    "Governments now subsidise domestic capacity, restrict exports of advanced tools and treat chip access as a national security question. For buyers, that means dual sourcing and long-term visibility are now part of hardware planning.",
                ],
            },
        ],
        "facts": [
            "Transistors are electrical switches with no moving parts.",
            "Modern process node numbers no longer map to a physical dimension.",
            "Advanced packaging is as important as transistor scaling today.",
            "Chip production is concentrated in a handful of companies and regions.",
        ],
        "faq": [
            {
                "q": "What is the difference between a chip and a semiconductor?",
                "a": "A semiconductor is the material. A chip, or integrated circuit, is a device built from that material containing many interconnected transistors.",
            },
            {
                "q": "Why is chip manufacturing so expensive?",
                "a": "Advanced lithography, cleanroom facilities, ultra-pure materials and years of process development cost billions, and the equipment is highly specialised.",
            },
            {
                "q": "Does Moore's law still hold?",
                "a": "Transistor counts are still rising but no longer double reliably every two years at lower cost. Gains now come from packaging, specialised architectures and software efficiency as much as scaling.",
            },
        ],
        "related": ["neuromorphiccomputing", "quantumcomputing", "artificialintelligence"],
    },
    {
        "slug": "robotics",
        "name": "Robotics",
        "short": "Robotics",
        "icon": "🤖",
        "category": "Emerging",
        "title": "Robotics Explained: Sensing, Control and AI",
        "meta": "How robots sense, decide and move, which kinds are in real use today, how AI is changing them, and the safety questions that come with autonomous machines.",
        "lede": "Robotics is the engineering of machines that sense their surroundings, decide what to do, and act physically on the world.",
        "image": "https://images.unsplash.com/photo-1727434032773-af3cd98375ba?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Robotics",
        "keywords": ["robotics", "how robots work", "industrial robots", "autonomous robots", "robot safety", "robot sensing"],
        "intro": [
            "A robot is a loop: sensors gather information, software decides, actuators produce motion, and the result changes what the sensors see next. Everything else is engineering detail, and the detail is where the difficulty lives.",
            "The field spans factory arms bolted to a floor, warehouse fleets navigating among people, surgical assistants, drones and humanoid research platforms. They share control problems but almost nothing else.",
        ],
        "sections": [
            {
                "id": "components",
                "h": "The parts of a robotic system",
                "p": [
                    "Sensors provide proprioception and perception: encoders measure joint position, inertial units measure orientation, cameras and depth sensors map the environment, and force sensors detect contact. Actuators convert energy into motion, usually electric motors with gearboxes, sometimes hydraulics.",
                    "Control closes the loop. A planner decides where to go, a controller computes the commands, and low-level servo loops keep the motion stable. Real-time constraints are strict: a late command is a wrong command.",
                ],
                "list": [
                    "Perception: cameras, LiDAR, depth, force and tactile sensing.",
                    "Localisation: knowing where the robot is in a map.",
                    "Planning: deciding a path or grasp that respects constraints.",
                    "Control: precise, stable execution at high update rates.",
                    "Actuation: motors, gearboxes, hydraulics and end effectors.",
                    "Safety: e-stops, force limits, guarded spaces and certified functions.",
                ],
            },
            {
                "id": "types",
                "h": "Where robots already work",
                "p": [
                    "Industrial arms perform welding, painting and assembly with repeatability no human can match. Warehouse robots move shelves and parcels. Autonomous mobile robots transport material in hospitals and factories.",
                    "Field robots inspect pipelines, mines and power lines. Surgical systems extend a surgeon's precision. Agricultural robots weed selectively, and drones survey land that would take days to walk.",
                ],
            },
            {
                "id": "ai",
                "h": "How AI is changing robotics",
                "p": [
                    "Classical robotics depends on accurate models of the world. Learning-based methods instead train policies from demonstration or simulation, which helps with tasks that are easy for a human and hard to program, such as picking a randomly oriented object from a bin.",
                    "Simulation lets teams train thousands of variations cheaply, and vision models improve perception in cluttered scenes. The bottleneck is the gap between simulation and reality, and the fact that learned behaviour is harder to certify for safety.",
                ],
                "callout": "Robots are impressive in structured environments and fragile in messy ones. That gap is the field's real frontier, not appearance.",
            },
            {
                "id": "safety",
                "h": "Safety and the human question",
                "p": [
                    "Any robot that can injure a person needs risk assessment, guarded zones or force-limited design, and an emergency stop that actually works. Collaborative robots are designed to slow or stop when contact is detected rather than to be separated by a fence.",
                    "Automation changes jobs more often than it deletes them: tasks shift towards supervision, maintenance and exception handling. The organisations that plan that transition explicitly handle it far better than those that assume it will sort itself out.",
                ],
            },
        ],
        "facts": [
            "Robotics is a sense-plan-act loop with hard real-time constraints.",
            "Industrial arms dominate real-world deployments by a wide margin.",
            "Simulation accelerates learning but does not eliminate the reality gap.",
            "Safety certification is the main barrier for autonomous machines near people.",
        ],
        "faq": [
            {
                "q": "Are robots about to take over factories?",
                "a": "They already do much of the repeatable work. Full lights-out manufacturing remains rare because handling exceptions, maintenance and changeovers still needs people.",
            },
            {
                "q": "What is a collaborative robot?",
                "a": "A robot designed to work alongside people, with force and speed limits and contact detection so that it can stop safely instead of being caged off.",
            },
            {
                "q": "Do robots need AI?",
                "a": "Not for repeatable tasks, which are usually handled by classical control. AI helps mainly with perception and manipulation in unpredictable environments.",
            },
        ],
        "related": ["artificialintelligence", "internetofthings", "digitaltwins"],
    },
    {
        "slug": "quantumcomputing",
        "name": "Quantum Computing",
        "short": "Quantum",
        "icon": "⚛️",
        "category": "Emerging",
        "title": "Quantum Computing Explained: Qubits and Reality",
        "meta": "How quantum computers use qubits, superposition and entanglement, what they may solve, and why post-quantum encryption matters now.",
        "lede": "A quantum computer uses the physics of very small systems to perform certain calculations in ways classical computers cannot do efficiently.",
        "image": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Quantum_computing",
        "keywords": ["quantum computing", "what is a qubit", "quantum supremacy", "post-quantum cryptography", "quantum algorithms"],
        "intro": [
            "A classical bit is 0 or 1. A qubit can hold a superposition of both, and a set of entangled qubits cannot be described by considering each one separately. That structure is where the computational advantage comes from.",
            "It is not a faster version of your laptop. Quantum computers are specialised machines with narrow strengths, and building one large enough and stable enough to matter remains the central engineering challenge.",
        ],
        "sections": [
            {
                "id": "qubits",
                "h": "Qubits, superposition and entanglement",
                "p": [
                    "A qubit is a quantum system with two measurable states, such as the spin of a particle or a current in a superconducting circuit. Before measurement it exists in a weighted combination of both, and measurement collapses it to one outcome with probabilities set by those weights.",
                    "Entanglement links qubits so that their joint state carries information the parts do not hold individually. Interference then makes some computational paths cancel and others reinforce, which is how a quantum algorithm extracts an answer.",
                ],
            },
            {
                "id": "limits",
                "h": "Why they are so hard to build",
                "p": [
                    "Quantum states are extremely fragile. Heat, vibration and stray electromagnetic fields cause errors, so many designs operate near absolute zero and still need error correction.",
                    "Error correction is expensive: a single reliable logical qubit can require many physical qubits. That is why demonstrations with hundreds of physical qubits do not automatically translate into useful computation.",
                ],
                "callout": "The meaningful metric is not qubit count but reliable logical qubits and the depth of circuit they can run before errors dominate.",
            },
            {
                "id": "algorithms",
                "h": "What quantum computers are actually good at",
                "p": [
                    "Known algorithms give provable speedups for factoring large numbers, searching unstructured data quadratically faster, and simulating quantum systems. Simulation is the most promising near-term application, with potential impact in chemistry and materials research.",
                    "Many business problems have no known quantum advantage. Portfolio optimisation and logistics are active research areas, but classical solvers keep improving too, so the goalposts move.",
                ],
                "list": [
                    "Shor's algorithm: factoring, which threatens widely used public-key cryptography.",
                    "Grover's algorithm: quadratic speedup for unstructured search.",
                    "Quantum simulation: chemistry, materials and drug discovery.",
                    "Optimisation: promising but not yet proven at scale.",
                ],
            },
            {
                "id": "crypto",
                "h": "The consequence you should act on now",
                "p": [
                    "Public-key cryptography depends on problems that a large enough quantum computer could solve. Data encrypted today can be stored and decrypted later, so long-lived secrets are already at risk in principle.",
                    "Post-quantum algorithms have been standardised and are being deployed. The practical step for most organisations is to inventory where public-key cryptography is used and plan migration, rather than wait for a working large-scale machine.",
                ],
            },
        ],
        "facts": [
            "Qubits exploit superposition and entanglement, not parallel classical bits.",
            "Error correction overhead is the main barrier to useful scale.",
            "Quantum simulation of molecules is the most credible near-term use.",
            "Post-quantum encryption migration is urgent for long-lived sensitive data.",
        ],
        "faq": [
            {
                "q": "Will quantum computers replace normal computers?",
                "a": "No. They excel at specific problem classes and are poor at ordinary tasks. Classical computers will keep running spreadsheets, video and most software.",
            },
            {
                "q": "How close are useful quantum computers?",
                "a": "Small systems can do real science today. Large, error-corrected machines capable of commercially significant work are still a research and engineering challenge with uncertain timing.",
            },
            {
                "q": "Should I worry about quantum attacks now?",
                "a": "Not about an attack tomorrow, but yes about planning. Long-lived confidential data and critical infrastructure should begin migrating to post-quantum cryptography now.",
            },
        ],
        "related": ["semiconductors", "cybersecurity", "artificialintelligence"],
    },
]
