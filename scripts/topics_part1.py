# Content data for the Tech Topic guide pages (part 1).
# Each entry renders to /<slug> via scripts/build_topics.py.

TOPICS = [
    {
        "slug": "artificialintelligence",
        "name": "Artificial Intelligence",
        "short": "AI",
        "icon": "🧠",
        "category": "Foundations",
        "title": "Artificial Intelligence Explained: How AI Works",
        "meta": "A clear guide to artificial intelligence: what AI really means, how modern systems learn, where it is already used, and the limits worth knowing in 2026.",
        "lede": "Artificial intelligence is the branch of computer science that builds systems able to do work we normally associate with human judgement, from understanding a sentence to recognising a face in a crowd.",
        "image": "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "keywords": ["artificial intelligence", "what is AI", "how AI works", "AI explained", "narrow AI", "generative AI"],
        "intro": [
            "Artificial intelligence (AI) is not a single product or a single technique. It is an umbrella term covering search algorithms, rule-based expert systems, machine learning, computer vision, natural language processing and robotics. What those approaches share is a goal: software that makes useful decisions in messy, open-ended situations.",
            "Almost every AI system you meet today is narrow AI. It is very good at one well-defined job and has no wider understanding. That distinction matters, because marketing language often blurs the line between a language model that writes an email and a general intelligence that could handle anything.",
        ],
        "sections": [
            {
                "id": "how-ai-works",
                "h": "How modern AI systems are built",
                "p": [
                    "Most contemporary AI is data-driven. A model is a very large collection of adjustable numbers plus a structure that decides how those numbers combine. Training adjusts the numbers until the model's output matches real examples closely enough to be useful. Once trained, the model answers new input in a single pass, which is called inference.",
                    "Deep learning stacks many layers of simple transformations to learn features that nobody had to hand-code, such as the edge of an object or the grammar of a sentence. Large language models push this further by learning statistical patterns across enormous text collections, which is why they can continue a prompt, answer a question or draft code.",
                ],
                "list": [
                    "Training data: the examples the model learns from, including their labels or surrounding context.",
                    "Architecture: the structure that decides what the model can represent at all.",
                    "Training: the expensive optimisation step that tunes the model's parameters.",
                    "Inference: the cheap, high-volume step that produces an answer for a user.",
                    "Evaluation and guardrails: tests, filters and human review that catch bad outputs.",
                ],
            },
            {
                "id": "ai-in-daily-life",
                "h": "Where AI is already part of your day",
                "p": [
                    "Search ranking, spam filtering, map routing, photo search, fraud checks, autocomplete, recommendation feeds and voice assistants are all AI systems. They are designed to disappear into the product, which is why the debate about AI can feel abstract even though the technology is already everywhere.",
                    "In business, AI shows up in demand forecasting, document processing, support triage, code assistance, quality inspection and medical imaging. The common thread is a repetitive decision that improves with pattern recognition at scale, not a job that needs to be replaced wholesale.",
                ],
            },
            {
                "id": "ai-limits",
                "h": "What AI still gets wrong",
                "p": [
                    "AI systems are confident, not correct. Language models can invent facts and citations, image models can produce impossible physics, and predictive models inherit the bias of their training data. Polished output makes errors harder to spot, not easier.",
                    "Sensible deployments keep a human in the loop for high-stakes decisions, log what the system was asked and what it answered, test for bias across groups, and tell users plainly when they are interacting with a machine.",
                ],
                "callout": "A useful rule of thumb: AI is strongest where a wrong answer is cheap to catch and weakest where a wrong answer is expensive to discover.",
            },
            {
                "id": "using-ai-well",
                "h": "How to use AI well",
                "p": [
                    "Treat AI as a fast junior collaborator rather than an oracle. Give it context, show it an example of what good looks like, ask it to explain its reasoning, and verify anything that would be costly to get wrong.",
                    "The people who get the most from these tools are not the ones with the cleverest prompts. They are the ones who understand the task well enough to judge the output quickly.",
                ],
                "list": [
                    "Start with a narrow, repeatable task instead of a vague ambition.",
                    "Feed in source material rather than relying on the model's memory.",
                    "Check names, numbers, dates and citations before publishing.",
                    "Keep confidential data out of tools you do not control.",
                    "Measure whether output actually saves time, not whether it looks impressive.",
                ],
            },
        ],
        "facts": [
            "AI is the umbrella term; machine learning is one approach inside it.",
            "Nearly all deployed systems are narrow AI built for a single task.",
            "Training a large model is expensive; running it is cheap and happens billions of times a day.",
            "Strong benchmark scores do not guarantee reliability in production.",
        ],
        "faq": [
            {
                "q": "What is the difference between AI and machine learning?",
                "a": "AI is the broad goal of making machines perform intelligent tasks. Machine learning is a family of methods that reach that goal by learning patterns from data. Deep learning is a subset of machine learning that uses multi-layer neural networks.",
            },
            {
                "q": "Is a chatbot really artificial intelligence?",
                "a": "Yes. A chat model is a narrow AI system trained mainly to predict and generate text. It is strong at language tasks and unreliable on verified facts unless it is given sources or tools.",
            },
            {
                "q": "Do I need to code to use AI?",
                "a": "No. Most useful applications today are plain-language tools and built-in features. Coding helps when you want automation, custom data pipelines or control over a model of your own.",
            },
            {
                "q": "Will AI replace whole jobs?",
                "a": "AI automates tasks far more reliably than entire roles. Work that is mostly routine text or pattern matching changes first, while judgement, accountability and human relationships remain with people.",
            },
        ],
        "related": ["machinelearning", "robotics", "bigdata"],
    },
    {
        "slug": "machinelearning",
        "name": "Machine Learning",
        "short": "ML",
        "icon": "📊",
        "category": "Foundations",
        "title": "Machine Learning Explained: Types and Limits",
        "meta": "How machine learning works: supervised, unsupervised and reinforcement learning, how models are trained and evaluated, and why projects fail.",
        "lede": "Machine learning is the part of AI where software improves from examples instead of following rules a person wrote by hand.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Machine_learning",
        "keywords": ["machine learning", "supervised learning", "unsupervised learning", "reinforcement learning", "model training", "overfitting"],
        "intro": [
            "Traditional software encodes logic: if this, then that. Machine learning flips the direction. You supply examples of inputs and desired outputs, and an algorithm searches for a rule that reproduces the pattern well enough to generalise to cases it has never seen.",
            "That shift is powerful and easy to overstate. A model can only learn what its data and its objective allow, and a model that looks excellent in testing can fail quietly in the real world.",
        ],
        "sections": [
            {
                "id": "learning-types",
                "h": "The main types of machine learning",
                "p": [
                    "Most practical work falls into three families. Supervised learning uses labelled examples to predict a category or a number. Unsupervised learning looks for structure without labels. Reinforcement learning trains an agent by rewarding behaviour over many attempts.",
                    "In between sit self-supervised methods, which generate their own labels from raw data and power most modern language and vision models, and semi-supervised methods that combine a small labelled set with a large unlabelled one.",
                ],
                "list": [
                    "Supervised: spam detection, credit risk scoring, defect detection, price prediction.",
                    "Unsupervised: customer segmentation, anomaly detection, topic discovery, compression.",
                    "Reinforcement: game playing, robot control, recommendation policies, scheduling.",
                    "Self-supervised: language models, image encoders, speech representations.",
                ],
            },
            {
                "id": "training",
                "h": "How a model is trained and evaluated",
                "p": [
                    "Training needs features, a target and a loss function that measures how wrong the model is. An optimiser repeatedly nudges the parameters to reduce that loss. The danger is memorising the training set instead of learning the underlying pattern, which is called overfitting.",
                    "The defence is honest evaluation: hold out data the model never sees, validate choices on a separate split, and report metrics that match the real cost of mistakes. Accuracy is misleading when one class dominates, so precision, recall and calibration often matter more.",
                ],
                "callout": "A model that is 99% accurate on balanced benchmark data can still be useless if the 1% it misses are exactly the cases your business cares about.",
            },
            {
                "id": "ml-in-practice",
                "h": "Where machine learning earns its keep",
                "p": [
                    "The strongest applications repeat at volume and tolerate some error. Sorting email, flagging unusual transactions, forecasting demand, prioritising support tickets, reading scanned documents and spotting defects on a production line all fit that description.",
                    "Fields where every decision is unique and consequences are severe, such as sentencing or diagnosis without oversight, demand far more caution. There the model becomes an assistant whose output is checked, not an authority.",
                ],
            },
            {
                "id": "limits",
                "h": "Why machine learning projects fail",
                "p": [
                    "The usual cause is not the algorithm. It is the data: too little of it, labels that disagree with each other, or a training set that does not resemble live traffic. The second most common cause is drift, where the world changes and the model silently keeps predicting the old one.",
                    "Successful teams start with a baseline they can beat, such as a simple rule or a human process, and only move to a complex model when the simpler version has been measured and beaten.",
                ],
                "list": [
                    "Define the decision the model supports before choosing any algorithm.",
                    "Audit labels: who created them, how consistently, and with what bias.",
                    "Monitor live inputs and outputs after launch, not just at training time.",
                    "Keep a simple baseline so improvements are provable.",
                    "Plan for retraining and for the day the model must be switched off.",
                ],
            },
        ],
        "facts": [
            "Machine learning is a subset of AI, and deep learning is a subset of machine learning.",
            "Overfitting is memorising training data; underfitting is failing to learn the pattern at all.",
            "Data quality usually matters more than model choice.",
            "Models degrade as the real world drifts away from their training data.",
        ],
        "faq": [
            {
                "q": "Is machine learning the same as AI?",
                "a": "No. AI is the broader goal of intelligent behaviour. Machine learning is one way to get there, by learning from data, and it is currently the dominant approach.",
            },
            {
                "q": "How much data does a model need?",
                "a": "It depends on the problem's complexity and the signal in the data. Simple tabular problems can work with thousands of rows, while image and language models often need millions of examples or a pretrained model to start from.",
            },
            {
                "q": "What is overfitting in plain language?",
                "a": "It is when a model learns the specific training examples too closely, including their noise, so it performs well on data it has seen and poorly on anything new.",
            },
        ],
        "related": ["artificialintelligence", "bigdata", "neuromorphiccomputing"],
    },
    {
        "slug": "bigdata",
        "name": "Big Data",
        "short": "Big Data",
        "icon": "💾",
        "category": "Foundations",
        "title": "Big Data Explained: The 5 Vs and Modern Data Stacks",
        "meta": "What big data means beyond the buzzword: the five Vs, how a modern data pipeline works, which tools teams actually use, and how to turn raw volume into decisions.",
        "lede": "Big data is data too large, too fast or too varied for the tools a team already had, which is why it forced a new generation of storage and processing systems.",
        "image": "https://images.unsplash.com/photo-1639322537228-f710d846310a?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Big_data",
        "keywords": ["big data", "data pipeline", "data lakehouse", "analytics", "the 5 Vs of big data", "data engineering"],
        "intro": [
            "Every organisation now produces more data than it can read by hand: clickstreams, logs, transactions, sensor readings, support tickets, video. Big data is the discipline of storing and processing that flow so it can answer questions at a scale spreadsheets cannot reach.",
            "The term is relative. For a small studio, a few million rows may already be big. What matters is whether the volume, speed or variety breaks the current tooling.",
        ],
        "sections": [
            {
                "id": "five-vs",
                "h": "The five Vs that define a data problem",
                "p": [
                    "Volume describes scale. Velocity describes how quickly data arrives and how fresh answers must be. Variety describes the mix of structured tables, semi-structured JSON and unstructured text, images or audio.",
                    "Two more Vs matter just as much in practice. Veracity asks whether the data is trustworthy, and value asks whether anyone will act on the result. A pipeline that produces elegant dashboards nobody reads is an expensive hobby.",
                ],
                "list": [
                    "Volume: terabytes to petabytes that no single machine should hold alone.",
                    "Velocity: streaming events that need processing within seconds.",
                    "Variety: tables, documents, media and logs in the same system.",
                    "Veracity: duplicates, missing fields and late-arriving records.",
                    "Value: a decision that changes because the data exists.",
                ],
            },
            {
                "id": "pipeline",
                "h": "How a modern data pipeline works",
                "p": [
                    "Data is ingested from applications and devices, landed in cheap durable storage, cleaned and modelled into trustworthy tables, then served to dashboards, models and products. Each stage owns a contract so that a change upstream does not silently corrupt everything downstream.",
                    "Batch processing runs on a schedule for reporting. Stream processing handles events continuously for alerts, live pricing and fraud detection. Most mature teams run both and treat the warehouse as the shared source of truth.",
                ],
            },
            {
                "id": "tools",
                "h": "The tools behind the stack",
                "p": [
                    "Object storage holds raw files cheaply. Distributed engines process them in parallel. Columnar warehouses answer analytical queries quickly, and lakehouse formats add table semantics on top of plain files. Message brokers carry streams, and transformation tools keep SQL models versioned like software.",
                    "Tool names change every few years; the layers do not. Understanding ingestion, storage, processing, modelling and serving will outlast any specific product.",
                ],
                "list": [
                    "Storage: object stores and table formats for raw and modelled data.",
                    "Processing: distributed batch engines and stream processors.",
                    "Warehouse: columnar analytics with SQL access for the whole team.",
                    "Transformation: version-controlled SQL and data tests.",
                    "Serving: dashboards, reverse ETL, APIs and feature stores for models.",
                ],
            },
            {
                "id": "governance",
                "h": "Privacy, quality and governance",
                "p": [
                    "Large data collections attract legal and ethical obligations. Personal data needs a lawful basis, a retention limit and access controls. Aggregation is not automatically anonymisation; combining datasets can re-identify people surprisingly easily.",
                    "Quality is a habit rather than a project: tests on freshness and uniqueness, alerts when a job fails, documentation of what each column means, and one clearly owned definition of metrics such as active user or revenue.",
                ],
                "callout": "Start with the question, not the lake. The most useful data platform is the smallest one that answers real questions reliably.",
            },
        ],
        "facts": [
            "Big data is defined by tooling limits, not by a fixed number of gigabytes.",
            "Batch and streaming solve different latency needs and usually coexist.",
            "Data quality failures cost more than storage ever does.",
            "Anonymised data can often be re-identified when combined with other sources.",
        ],
        "faq": [
            {
                "q": "Is big data still relevant now that storage is cheap?",
                "a": "Yes. Storage got cheaper, but processing cost, data quality, governance and latency are still real constraints, and the skills to model data well remain scarce.",
            },
            {
                "q": "What is a data lakehouse?",
                "a": "A lakehouse stores data as open files in object storage while adding table features such as schemas, transactions and time travel. It aims to combine the flexibility of a data lake with the reliability of a warehouse.",
            },
            {
                "q": "Do small businesses need big data tools?",
                "a": "Usually not. A managed warehouse and a handful of well-modelled tables will outperform a complex distributed stack for most small teams.",
            },
        ],
        "related": ["machinelearning", "cloudcomputing", "edgecomputing"],
    },
    {
        "slug": "blockchain",
        "name": "Blockchain",
        "short": "Blockchain",
        "icon": "⛓️",
        "category": "Web3",
        "title": "Blockchain Explained: How Distributed Ledgers Work",
        "meta": "How blockchain works without a central authority: blocks, hashes, consensus, smart contracts, genuine use cases, and the limits behind the hype.",
        "lede": "A blockchain is a shared record that many independent participants maintain together, so no single party can quietly rewrite history.",
        "image": "https://images.unsplash.com/photo-1639322537228-f710d846310a?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Blockchain",
        "keywords": ["blockchain", "how blockchain works", "distributed ledger", "smart contracts", "consensus", "blockchain use cases"],
        "intro": [
            "A blockchain stores records in blocks that are cryptographically linked to the block before them. Changing an old entry changes its hash, which breaks every link that follows, so tampering is immediately visible to everyone holding a copy.",
            "The interesting part is not the chain. It is the agreement. A network of participants that do not fully trust each other can settle on one shared history using a consensus rule, without appointing an administrator.",
        ],
        "sections": [
            {
                "id": "how-it-works",
                "h": "Blocks, hashes and consensus",
                "p": [
                    "Each block contains transactions, a timestamp and the hash of the previous block. Nodes validate new blocks against the protocol rules before accepting them. If two valid histories appear, the network's consensus rule decides which one wins.",
                    "Proof of work secures a chain with computational effort. Proof of stake secures it with economic collateral that can be forfeited for misbehaviour. Both trade off differently in energy use, hardware requirements and how power is distributed among participants.",
                ],
                "list": [
                    "Public chains: anyone can read, validate and transact.",
                    "Private and consortium chains: a known group runs the validators.",
                    "Smart contracts: programs that execute automatically when conditions are met.",
                    "Finality: how long until a transaction is practically irreversible.",
                ],
            },
            {
                "id": "use-cases",
                "h": "Where a blockchain genuinely helps",
                "p": [
                    "Blockchains are strongest when several parties need one shared record but no party is trusted to own it, and when an audit trail must survive disagreement. Cross-border settlement, trade finance, provenance tracking and tokenised assets fit that shape.",
                    "Where a trusted operator already exists, a normal database is faster, cheaper and easier to govern. Adding a chain there usually adds complexity without adding trust.",
                ],
            },
            {
                "id": "limits",
                "h": "The practical limits",
                "p": [
                    "Public chains are slower and more expensive per transaction than centralised databases because every validator repeats the work. Throughput has improved with layer-two networks, but trade-offs in cost, complexity and security remain.",
                    "Users also carry burdens that banks used to absorb: key management, irreversible mistakes, scams and unclear legal recourse. Regulation is still catching up in most jurisdictions.",
                ],
                "callout": "Ask who benefits from removing the middleman. If the answer is nobody with a budget, a shared database is the better engineering choice.",
            },
            {
                "id": "evaluating",
                "h": "How to evaluate a blockchain claim",
                "p": [
                    "Check whether the ledger must be public, whether participants are known, and who can reverse a mistaken transaction. Read the token design carefully, because many projects use a chain mainly to sell a token rather than to solve a coordination problem.",
                    "For users, the safety basics matter more than the technology: verify contract addresses, never share a seed phrase, treat unsolicited offers as hostile, and assume that a signed transaction cannot be undone.",
                ],
            },
        ],
        "facts": [
            "Cryptographic linking makes tampering evident, not impossible.",
            "Consensus is what makes a distributed ledger trustworthy.",
            "Smart contracts are code, and code has bugs that are often irreversible.",
            "A trusted central operator usually makes a blockchain unnecessary.",
        ],
        "faq": [
            {
                "q": "Is blockchain the same as Bitcoin?",
                "a": "No. Bitcoin is one application of blockchain technology, a digital currency with its own consensus rules. Many other chains and designs exist, including some without a currency.",
            },
            {
                "q": "Can blockchain data be deleted?",
                "a": "Not easily. Most public chains are append-only, which conflicts with privacy rules that require deletion. This is a serious obstacle for storing personal data directly on chain.",
            },
            {
                "q": "Are smart contracts legally binding?",
                "a": "That depends on jurisdiction. Many courts now consider them enforceable agreements, but consumer protection, dispute resolution and liability are still governed by ordinary law.",
            },
        ],
        "related": ["web3", "cybersecurity", "opensource"],
    },
    {
        "slug": "web3",
        "name": "Web3",
        "short": "Web3",
        "icon": "🕸️",
        "category": "Web3",
        "title": "Web3 Explained: Wallets, Smart Contracts and Reality",
        "meta": "What Web3 means beyond the marketing: wallets, smart contracts, dApps and tokens, which parts work today, and the risks users should understand first.",
        "lede": "Web3 describes an idea of the internet where users hold their own identity and assets in wallets instead of renting an account from a platform.",
        "image": "https://images.unsplash.com/photo-1639322537228-f710d846310a?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Web3",
        "keywords": ["web3", "what is web3", "smart contracts", "dApps", "crypto wallets", "decentralised web"],
        "intro": [
            "The first web was read-only pages. The second web made publishing and social interaction easy, but concentrated identity, distribution and payments inside a handful of platforms. Web3 is a proposal to move ownership of accounts, assets and data to users through public blockchains.",
            "It is a direction of travel rather than a finished product. Some pieces, such as self-custody wallets and stablecoin payments, work at scale. Others, such as fully decentralised social networks, remain experiments with small user bases.",
        ],
        "sections": [
            {
                "id": "building-blocks",
                "h": "The building blocks",
                "p": [
                    "A wallet is a key manager. It holds the private key that proves ownership and signs transactions; the balance lives on chain, not in the app. Smart contracts are programs deployed to a chain that run exactly as written, which makes them composable and unforgiving.",
                    "Decentralised applications combine a smart contract backend with an ordinary web frontend. Tokens represent assets, access or governance rights, and decentralised autonomous organisations coordinate groups through on-chain voting.",
                ],
                "list": [
                    "Wallet: your keys, your identity, your responsibility.",
                    "Smart contract: deterministic code that holds value and logic.",
                    "dApp: a normal interface talking to an on-chain backend.",
                    "Token: a transferable claim, often for access or governance.",
                    "DAO: shared treasury and rules enforced by code and votes.",
                ],
            },
            {
                "id": "what-works",
                "h": "What actually works today",
                "p": [
                    "Payments across borders, self-custody savings, tokenised funds and on-chain settlement between businesses are live and growing. Public block explorers also give a level of transparency that traditional finance rarely offers.",
                    "Consumer social and gaming experiments struggle because the experience is slower and more expensive than centralised alternatives, and because most users do not want to manage keys. That may change, but it has not yet.",
                ],
            },
            {
                "id": "risks",
                "h": "The risks are mostly human and legal",
                "p": [
                    "Lost keys are lost funds, with no support line. Approving a malicious contract can drain a wallet. Phishing sites look identical to real ones, and social engineering is the dominant attack path, not breaking cryptography.",
                    "Regulation of tokens, taxes and liability varies by country and is still shifting. Before moving real money, check local rules and treat every unsolicited message as a potential scam.",
                ],
                "callout": "In Web3 the security model is inverted: you are the bank, so you are also the fraud department.",
            },
            {
                "id": "should-you-care",
                "h": "Who should pay attention",
                "p": [
                    "Developers benefit from learning how wallets, signatures and contracts work, because the same primitives now appear in mainstream payments and identity products. Businesses should watch settlement and tokenisation, where the cost savings are concrete.",
                    "Casual users can safely ignore most of it until a specific product solves a specific problem for them. Curiosity is healthy; speculative urgency is not.",
                ],
            },
        ],
        "facts": [
            "A wallet stores keys, not coins.",
            "Public blockchains are transparent, which cuts both ways for privacy.",
            "Most losses come from phishing and key mismanagement, not broken cryptography.",
            "Token regulation differs widely and keeps changing.",
        ],
        "faq": [
            {
                "q": "Is Web3 the same as crypto?",
                "a": "They overlap heavily. Crypto usually refers to the currencies and trading markets, while Web3 describes the wider set of applications built on wallets and blockchains.",
            },
            {
                "q": "Do I need a wallet to use Web3?",
                "a": "Yes, for anything that involves signing or holding assets. Browsers and mobile apps provide wallet software, but you remain responsible for backing up the recovery phrase.",
            },
            {
                "q": "Is Web3 anonymous?",
                "a": "No. Public chain activity is permanently visible and can often be linked to real identities through exchanges and analytics. It is pseudonymous at best.",
            },
        ],
        "related": ["blockchain", "cybersecurity", "artificialintelligence"],
    },
    {
        "slug": "cloudcomputing",
        "name": "Cloud Computing",
        "short": "Cloud",
        "icon": "☁️",
        "category": "Infrastructure",
        "title": "Cloud Computing Explained: IaaS, PaaS and SaaS",
        "meta": "Cloud computing in plain language: service and deployment models, how pay-as-you-go pricing really works, and what to check before moving workloads to the cloud.",
        "lede": "Cloud computing means renting computing power, storage and services over the internet instead of owning the hardware that provides them.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Cloud_computing",
        "keywords": ["cloud computing", "IaaS PaaS SaaS", "cloud migration", "cloud costs", "public cloud", "hybrid cloud"],
        "intro": [
            "A cloud provider runs large data centres and sells access to them in small, elastic units. You get a server in minutes instead of a procurement cycle, and you can release it when the traffic drops.",
            "The trade is control for convenience. Someone else owns the hardware, the network and often the platform, and you pay for that with a monthly bill and a set of shared responsibilities.",
        ],
        "sections": [
            {
                "id": "service-models",
                "h": "The three service models",
                "p": [
                    "Infrastructure as a service gives you virtual machines, storage and networks. You manage the operating system and everything above it. Platform as a service gives you a runtime and managed services, so you deploy code and let the provider patch the platform. Software as a service gives you a finished product such as email or a CRM.",
                    "The model you choose decides how much of the stack you operate. Most real systems mix all three: SaaS for collaboration, PaaS for application hosting, IaaS for workloads that need full control.",
                ],
                "list": [
                    "IaaS: maximum control, maximum operational work.",
                    "PaaS: fastest path from code to running service.",
                    "SaaS: no operations, least customisation.",
                    "Serverless: per-request execution with almost no infrastructure to manage.",
                ],
            },
            {
                "id": "deployment",
                "h": "Public, private and hybrid",
                "p": [
                    "Public cloud shares infrastructure across customers with strong logical isolation. Private cloud keeps a dedicated environment, usually for regulatory or latency reasons. Hybrid connects both so sensitive data can stay on premises while elastic workloads run elsewhere.",
                    "Multi-cloud spreads risk and avoids lock-in but multiplies operational complexity. It works best when there is a clear reason, such as a specific regional requirement or a service only one provider offers.",
                ],
            },
            {
                "id": "economics",
                "h": "How cloud economics actually work",
                "p": [
                    "Pricing is metered: compute by the second, storage by the gigabyte-month, and data transfer by the gigabyte. The last one surprises people, because moving data out of a provider is often the most expensive line item and the hardest to negotiate.",
                    "Elasticity rewards discipline. Idle resources still bill, oversized instances still bill, and forgotten snapshots still bill. Tagging resources, setting budgets and reviewing spend monthly usually saves more than any architectural rewrite.",
                ],
                "callout": "The cloud is cheaper than owning hardware only when utilisation is variable. A steady, predictable workload can be cheaper on dedicated servers.",
            },
            {
                "id": "security",
                "h": "Security is shared, not outsourced",
                "p": [
                    "Providers secure the physical facilities, hardware and hypervisor. You secure identity, configuration, data and access. Misconfigured storage and stolen credentials cause most cloud incidents, not provider breaches.",
                    "Start with strong identity: multi-factor authentication, least-privilege roles and short-lived credentials. Then encrypt data at rest and in transit, log administrative actions, and test backups by actually restoring them.",
                ],
            },
        ],
        "facts": [
            "Cloud shifts spending from capital expense to operating expense.",
            "Data egress is often the largest hidden cost.",
            "Most breaches come from customer misconfiguration, not provider failure.",
            "Reserved and spot capacity can cut compute costs substantially for predictable work.",
        ],
        "faq": [
            {
                "q": "Is the cloud always cheaper?",
                "a": "No. It is cheaper when demand is variable and you can shut resources down. Steady, high-utilisation workloads are often cheaper on owned or dedicated hardware.",
            },
            {
                "q": "What does vendor lock-in really mean?",
                "a": "It means the cost of leaving rises because your code depends on proprietary services, data formats or identity systems. Managed services are worth it when the lock-in is a deliberate, priced trade-off.",
            },
            {
                "q": "Who is responsible for cloud security?",
                "a": "Both parties. The provider secures the infrastructure; you secure your configuration, identities, applications and data.",
            },
        ],
        "related": ["serverlesscomputing", "edgecomputing", "devops"],
    },
]
