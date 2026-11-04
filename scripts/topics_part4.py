# Content data for the Tech Topic guide pages (part 4).

TOPICS = [
    {
        "slug": "neuromorphiccomputing",
        "name": "Neuromorphic Computing",
        "short": "Neuromorphic",
        "icon": "🧩",
        "category": "Emerging",
        "title": "Neuromorphic Computing: Chips That Work Like Brains",
        "meta": "How neuromorphic chips use spiking neurons and event-driven computation to cut power use, where they help today, and why they are not general-purpose processors.",
        "lede": "Neuromorphic computing designs hardware around the way nervous systems process information, using sparse spikes instead of constant clocked calculation.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Neuromorphic_engineering",
        "keywords": ["neuromorphic computing", "spiking neural networks", "brain-inspired chips", "low power AI", "event cameras", "edge AI hardware"],
        "intro": [
            "A conventional processor computes continuously on a clock, moving numbers between memory and logic. A brain does something different: neurons stay quiet until a signal arrives, then fire a brief spike. Most of the system is idle most of the time.",
            "Neuromorphic engineering copies that idea in silicon. Computation is event-driven, memory and processing sit together, and information travels as spikes. The prize is dramatically lower energy use for certain kinds of sensing and inference.",
        ],
        "sections": [
            {
                "id": "principles",
                "h": "The principles it borrows from biology",
                "p": [
                    "Spiking neurons integrate input over time and fire when a threshold is crossed. Because a spike carries only timing information, silence costs almost nothing. That sparsity is the source of the efficiency advantage.",
                    "Co-locating memory and computation avoids the energy spent shuttling data across a bus, which dominates power use in conventional AI accelerators. Learning rules are often local, adjusting a synapse based only on the neurons it connects, rather than requiring a global backward pass.",
                ],
                "list": [
                    "Event-driven: no clock, no work without input.",
                    "Sparse: few neurons active at once.",
                    "In-memory compute: weights stored where they are used.",
                    "Local learning: updates that do not need the whole network.",
                    "Temporal coding: time itself carries information.",
                ],
            },
            {
                "id": "hardware",
                "h": "What neuromorphic hardware looks like",
                "p": [
                    "Research and commercial chips arrange many small neuron-like cores with on-chip memory and a network that routes spikes. Some are digital and deterministic, which makes them easier to program; others are analogue and more energy-efficient but harder to reproduce precisely.",
                    "Event cameras are a natural partner. Instead of capturing full frames thirty times a second, each pixel reports only when brightness changes, producing a sparse stream that is cheap to process and has very low latency.",
                ],
            },
            {
                "id": "uses",
                "h": "Where it is being used",
                "p": [
                    "The strongest fits are always-on sensing at the edge: wake-word detection, gesture recognition, vibration monitoring, drone navigation and visual tracking in battery-powered devices. These need continuous awareness with a power budget measured in milliwatts.",
                    "Robotics benefits from the tight sensor-to-action loop. Medical devices and wearables benefit from low power and local processing that keeps data on the device.",
                ],
                "callout": "Neuromorphic computing is not trying to beat a GPU at training a large language model. It is trying to make small, continuous perception almost free.",
            },
            {
                "id": "limits",
                "h": "Why it has not replaced anything yet",
                "p": [
                    "Programming models are immature. Standard deep learning frameworks assume dense tensors and backpropagation, while spiking networks need new abstractions, compilers and debugging tools. Porting an existing model is not a button press.",
                    "Accuracy on mainstream benchmarks can lag conventional networks, and analogue designs face noise and variability. The technology is advancing through specific embedded applications rather than a broad takeover.",
                ],
            },
        ],
        "facts": [
            "Neuromorphic chips compute with sparse timing events rather than a clock.",
            "Co-locating memory and compute is central to their efficiency.",
            "Always-on edge sensing is the most credible near-term application.",
            "Software tooling, not physics, is the main adoption barrier.",
        ],
        "faq": [
            {
                "q": "Is neuromorphic computing the same as quantum computing?",
                "a": "No. Neuromorphic chips are classical devices inspired by biological neurons. Quantum computers exploit quantum mechanics. The two are unrelated approaches.",
            },
            {
                "q": "Can neuromorphic chips run ChatGPT-style models?",
                "a": "Not currently at comparable scale or convenience. They are designed for sparse, event-driven workloads, while large language models rely on dense matrix operations on conventional accelerators.",
            },
            {
                "q": "Why does event-driven design save energy?",
                "a": "Because idle components consume almost nothing. Work happens only when a signal arrives, unlike clocked hardware that burns power on every cycle regardless of activity.",
            },
        ],
        "related": ["artificialintelligence", "semiconductors", "edgecomputing"],
    },
    {
        "slug": "virtualreality",
        "name": "VR & AR",
        "short": "VR & AR",
        "icon": "🥽",
        "category": "Emerging",
        "title": "VR and AR Explained: Immersive Computing Today",
        "meta": "The difference between virtual, augmented and mixed reality, how the headsets work, where the technology is genuinely useful, and what still holds it back.",
        "lede": "Virtual reality replaces what you see with a simulated world, while augmented reality layers digital information over the real one.",
        "image": "https://images.unsplash.com/photo-1694903110330-cc64b7e1d21d?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Virtual_reality",
        "keywords": ["virtual reality", "augmented reality", "VR vs AR", "mixed reality", "spatial computing", "XR headsets"],
        "intro": [
            "Both technologies rely on the same core trick: tracking where your head and hands are, then rendering the right image quickly enough that your brain accepts it as real. Get the latency wrong and the illusion collapses into nausea.",
            "Together with mixed reality they are often grouped as extended reality, or XR. The category has survived several hype cycles; the useful question is which applications survived with it.",
        ],
        "sections": [
            {
                "id": "differences",
                "h": "VR, AR and MR in one paragraph each",
                "p": [
                    "VR uses an opaque headset and full immersion, usually with tracked controllers and room-scale movement. AR keeps you in the real world and overlays graphics, either through a phone screen or transparent glasses. Mixed reality anchors virtual objects so they behave as if physically present, including occlusion and lighting.",
                    "The technical demands differ. VR controls everything the user sees, so realism can be stylised. AR must understand the real scene well enough to place objects convincingly, which is a much harder perception problem.",
                ],
                "list": [
                    "VR: training, gaming, design review, exposure therapy.",
                    "AR: navigation overlays, maintenance instructions, retail previews.",
                    "MR: collaborative 3D work, industrial assembly, surgical planning.",
                    "Spatial computing: interfaces driven by gaze, gesture and voice.",
                ],
            },
            {
                "id": "hardware",
                "h": "What is inside a headset",
                "p": [
                    "Displays, lenses, inertial sensors, cameras, depth sensors and a processor all fit into something worn on the face. Inside-out tracking uses cameras to locate the headset in the room without external base stations.",
                    "Comfort is a hardware problem. Resolution per eye, field of view, refresh rate, weight distribution, battery life and heat all compete for the same small volume. Passthrough cameras for mixed reality add latency and calibration challenges.",
                ],
            },
            {
                "id": "uses",
                "h": "Where it earns its place",
                "p": [
                    "The clearest return on investment is training for situations that are expensive or dangerous to rehearse: aircraft maintenance, surgical technique, industrial safety and emergency response. Practising repeatedly in simulation beats reading a manual.",
                    "Design review is another strong case, because a team can stand around a full-size model before anything is built. In consumer markets, gaming and fitness have the most durable audiences.",
                ],
                "callout": "The killer app for XR has consistently been training and visualisation, not casual entertainment.",
            },
            {
                "id": "barriers",
                "h": "What still holds it back",
                "p": [
                    "Headsets remain heavy enough to limit sessions, content libraries are fragmented across platforms, and developing spatial applications costs more than web or mobile equivalents. Comfort varies enormously between people, and a meaningful minority experience motion sickness.",
                    "Social norms matter too. People are reluctant to wear a headset in front of others, which limits everyday use even when the hardware is capable.",
                ],
            },
        ],
        "facts": [
            "AR overlays the real world; VR replaces it.",
            "Inside-out tracking removed the need for external base stations.",
            "Training and design review give the strongest business returns.",
            "Weight, battery and comfort still limit session length.",
        ],
        "faq": [
            {
                "q": "Is VR bad for your eyes?",
                "a": "Research has not shown permanent damage from normal use, but eye strain and fatigue are common. Taking breaks and ensuring correct lens spacing reduce discomfort.",
            },
            {
                "q": "Do you need a powerful PC for VR?",
                "a": "Standalone headsets run their own software and need nothing else. PC-connected headsets offer higher fidelity but require a strong graphics card.",
            },
            {
                "q": "Will AR glasses replace phones?",
                "a": "Not soon. Battery, heat, optics and social acceptance all constrain glasses. Phones are likely to remain the primary device while glasses handle specific tasks.",
            },
        ],
        "related": ["5gnetworks", "digitaltwins", "artificialintelligence"],
    },
    {
        "slug": "digitaltwins",
        "name": "Digital Twins",
        "short": "Digital Twins",
        "icon": "🪞",
        "category": "Emerging",
        "title": "Digital Twins Explained: Virtual Replicas",
        "meta": "What a digital twin is, how live data keeps it in sync, where twins are used in manufacturing, cities and healthcare, and how to start one without overbuilding.",
        "lede": "A digital twin is a virtual model of a real object, process or place, kept up to date with data so it can be used to predict, test and improve the real thing.",
        "image": "https://images.unsplash.com/photo-1727434032773-af3cd98375ba?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Digital_twin",
        "keywords": ["digital twin", "what is a digital twin", "digital twin manufacturing", "simulation", "predictive maintenance", "smart city"],
        "intro": [
            "A simulation runs a scenario. A digital twin stays connected to its physical counterpart, absorbing measurements and reflecting its current state, so answers are grounded in what is actually happening.",
            "That connection is the whole point. A twin without live data is just a model, however detailed.",
        ],
        "sections": [
            {
                "id": "how-it-works",
                "h": "How a twin stays in sync",
                "p": [
                    "Sensors stream measurements into a data platform. A physics or statistical model consumes them, updates its state, and produces outputs such as remaining useful life, predicted throughput or thermal risk. Visualisation layers make those outputs understandable to people.",
                    "Twins vary in fidelity. A simple spreadsheet-based model with a daily feed can be a twin. So can a high-fidelity simulation of an engine running in real time alongside test hardware. Start with the lowest fidelity that answers the question.",
                ],
                "list": [
                    "Asset: the physical thing being modelled.",
                    "Data: sensor feeds, maintenance records, design specifications.",
                    "Model: physics, statistics or machine learning, or a blend.",
                    "Synchronisation: how often state is updated and how drift is handled.",
                    "Use: prediction, optimisation, training or scenario testing.",
                ],
            },
            {
                "id": "uses",
                "h": "Where twins are used",
                "p": [
                    "Manufacturing twins predict equipment failure and optimise line balancing. Buildings tune energy use against occupancy and weather. Cities model traffic, flooding and infrastructure maintenance. Healthcare explores patient-specific models for treatment planning.",
                    "Wind farms and aircraft engines use twins to plan maintenance around actual wear rather than fixed schedules, which reduces both downtime and unnecessary servicing.",
                ],
            },
            {
                "id": "building",
                "h": "Starting a twin without overbuilding",
                "p": [
                    "Begin with one asset, one decision and one measurable outcome. Assemble the data you already have before buying sensors, and validate the model against known outcomes rather than its visual polish.",
                    "Governance matters as much as modelling. Someone must own the twin, define what counts as accurate, and decide what happens when the model disagrees with an experienced operator.",
                ],
                "callout": "If nobody would change a decision based on the twin's output, the twin is a demonstration, not a tool.",
            },
            {
                "id": "limits",
                "h": "The hard parts",
                "p": [
                    "Models drift as equipment ages and conditions change, so twins need recalibration and version history. Data quality, sensor coverage and integration with legacy systems usually absorb more effort than the simulation itself.",
                    "Costs accumulate in maintenance: a twin is another system to secure, patch and explain. Retire twins that no longer drive decisions.",
                ],
            },
        ],
        "facts": [
            "Live data, not visual fidelity, distinguishes a twin from a model.",
            "The best first twin targets a single decision with a measurable outcome.",
            "Twins need recalibration as the real asset changes.",
            "Most effort goes into data integration and governance, not simulation.",
        ],
        "faq": [
            {
                "q": "Is a digital twin just a 3D model?",
                "a": "No. A 3D model is a visual representation. A twin connects to data and models behaviour, so it can answer questions about the real asset's condition and future.",
            },
            {
                "q": "Do digital twins need AI?",
                "a": "Not necessarily. Physics-based models often do the work, especially where data is limited. Machine learning helps when relationships are too complex to model analytically.",
            },
            {
                "q": "What does a digital twin cost?",
                "a": "Costs range from a modest dashboard fed by existing data to multi-million programmes with real-time simulation. Start small and scale only after the decision value is proven.",
            },
        ],
        "related": ["internetofthings", "artificialintelligence", "virtualreality"],
    },
    {
        "slug": "3dprinting",
        "name": "3D Printing",
        "short": "3D Printing",
        "icon": "🖨️",
        "category": "Hardware",
        "title": "3D Printing Explained: Processes, Materials, Limits",
        "meta": "How 3D printing builds objects layer by layer, how FDM, resin and metal processes differ, and when additive manufacturing wins.",
        "lede": "3D printing, or additive manufacturing, builds an object from a digital model by adding material one layer at a time instead of cutting it away.",
        "image": "https://images.unsplash.com/photo-1727434032773-af3cd98375ba?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/3D_printing",
        "keywords": ["3D printing", "additive manufacturing", "FDM", "resin printing", "metal 3D printing", "rapid prototyping"],
        "intro": [
            "Subtractive manufacturing removes material from a block. Additive manufacturing does the opposite, which means complexity is nearly free: a lattice or an internal channel costs no more than a solid shape of the same volume.",
            "That makes 3D printing valuable where parts are customised, lightweight, geometrically complex or needed in small quantities. It is rarely the cheapest way to make a million identical objects.",
        ],
        "sections": [
            {
                "id": "processes",
                "h": "The main printing processes",
                "p": [
                    "Fused deposition modelling extrudes melted filament layer by layer. It is cheap, robust and widely used for prototypes and jigs. Resin processes cure liquid photopolymer with light, producing fine detail for models, dental work and small precision parts.",
                    "Powder bed fusion sinters or melts polymer or metal powder, allowing complex geometry without support structures. Binder jetting and material jetting deposit liquid binders or droplets. Metal printing is used for aerospace brackets, medical implants and replacement parts.",
                ],
                "list": [
                    "FDM: cheapest, strongest common option, visible layer lines.",
                    "Resin (SLA/MSLA/DLP): high detail, brittle unless engineered resin.",
                    "SLS/MJF: tough nylon parts, no supports, good for small batches.",
                    "Metal (LPBF/DED): dense functional parts, expensive and post-processed.",
                    "Binder jetting: fast, good for sand casting and some ceramics.",
                ],
            },
            {
                "id": "workflow",
                "h": "From model to object",
                "p": [
                    "The workflow starts with a CAD model, then slicing software converts it into toolpaths and parameters. Orientation decides strength, surface finish and how much support material is needed.",
                    "Post-processing is often the slowest step: removing supports, curing, sanding, machining or heat treating. Design for the process from the beginning instead of trying to print an assembly unchanged.",
                ],
            },
            {
                "id": "where",
                "h": "Where additive manufacturing wins",
                "p": [
                    "Rapid prototyping is the largest use, because design iteration becomes hours instead of weeks. Custom medical devices, dental aligners and hearing aids use the technology at real scale.",
                    "Spare parts and low-volume production benefit because no tooling is required. Lightweight lattice structures reduce fuel use in aerospace, and conformal cooling channels improve injection moulding.",
                ],
                "callout": "Use additive manufacturing when complexity, customisation or lead time matter more than unit cost.",
            },
            {
                "id": "limits",
                "h": "What it is not good at",
                "p": [
                    "Per-part cost stays high compared with injection moulding at volume, surface finish varies, and material properties can differ from the same plastic made conventionally. Certification for critical parts requires extensive testing.",
                    "The technology also shifts skill requirements: someone must understand tolerances, orientation and process limits, or prints fail in ways that look like design mistakes.",
                ],
            },
        ],
        "facts": [
            "Additive manufacturing makes geometric complexity nearly free.",
            "FDM dominates hobby and prototyping use; metal printing is industrial.",
            "Post-processing is frequently the bottleneck.",
            "Tooling-free production wins at low volume, not at mass production.",
        ],
        "faq": [
            {
                "q": "Is 3D printing strong enough for real parts?",
                "a": "Often yes, if the process and material match the load. Engineered filaments, nylon powder parts and metal printing are used in production, but certification depends on the application.",
            },
            {
                "q": "Why is 3D printing slow?",
                "a": "Material is deposited or fused one layer at a time, so time scales with height and volume. Industrial machines with many lasers or faster curing reduce this, at a much higher cost.",
            },
            {
                "q": "Can you 3D print a house?",
                "a": "Yes, with large gantry systems that extrude concrete. It suits simple walls and rapid builds, though reinforcement, plumbing and finishing still need conventional work.",
            },
        ],
        "related": ["robotics", "biotechnology", "greentechnology"],
    },
    {
        "slug": "biotechnology",
        "name": "Biotechnology",
        "short": "Biotech",
        "icon": "🧬",
        "category": "Emerging",
        "title": "Biotechnology Explained: CRISPR and Biomanufacturing",
        "meta": "How biotechnology uses living systems to make medicines, food and materials, what CRISPR changed, and the ethical and regulatory questions that come with it.",
        "lede": "Biotechnology applies living systems and the tools of molecular biology to make products, from medicines and vaccines to enzymes, materials and food.",
        "image": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Biotechnology",
        "keywords": ["biotechnology", "CRISPR", "gene editing", "biomanufacturing", "synthetic biology", "biotech explained"],
        "intro": [
            "Humans have used biology to make bread, beer and cheese for millennia. Modern biotechnology adds precision: reading and writing DNA, engineering proteins, and growing cells in controlled conditions.",
            "The result is a field that spans medicine, agriculture, materials and manufacturing, with timelines measured in years and a regulatory burden that reflects how directly it touches human health.",
        ],
        "sections": [
            {
                "id": "tools",
                "h": "The core tools",
                "p": [
                    "DNA sequencing reads genetic information quickly and cheaply. Synthesis writes DNA to order. CRISPR and related editors make targeted changes, while older techniques such as PCR amplify specific sequences for testing.",
                    "Bioinformatics ties it together, using computation to compare genomes, predict protein structures and design experiments. Machine learning has accelerated protein design and analysis considerably.",
                ],
                "list": [
                    "Sequencing: reading genomes and detecting variants.",
                    "Synthesis: building DNA and genes to specification.",
                    "CRISPR: targeted editing guided by a short RNA sequence.",
                    "Cell culture and fermentation: producing molecules at scale.",
                    "Bioinformatics: computational analysis and protein design.",
                ],
            },
            {
                "id": "applications",
                "h": "Where it is making a difference",
                "p": [
                    "Medicine is the most visible area: vaccines designed in weeks, monoclonal antibodies, gene therapies for rare diseases and diagnostic tests that read a pathogen's genetic signature. Personalised cancer treatment uses a patient's own tumour profile to choose therapy.",
                    "Beyond health, engineered microbes produce enzymes, flavours, fuels and materials. Plant breeding uses editing to improve disease resistance, and biomanufacturing aims to replace petrochemical routes for some chemicals.",
                ],
            },
            {
                "id": "ethics",
                "h": "Ethics, safety and regulation",
                "p": [
                    "Editing somatic cells affects only the patient. Editing embryos or germline cells would be inherited, which is why it is prohibited or tightly restricted in most countries. Off-target edits, mosaicism and long-term effects are active safety questions.",
                    "Regulation is strict because the products are living or biological. Clinical trials, environmental assessments and labelling rules exist to make the risks visible before products reach people.",
                ],
                "callout": "The technology is not the bottleneck in most biotech debates. The hard questions are about consent, equity, access and who decides what counts as an acceptable risk.",
            },
            {
                "id": "outlook",
                "h": "What to watch next",
                "p": [
                    "Cost curves are the story. Sequencing, synthesis and lab automation keep getting cheaper, which lowers the barrier for smaller labs and startups. AI-designed proteins are moving from papers into pipelines.",
                    "Realistically, most breakthroughs take a decade to become products. Announcements about curing a disease in cells or mice are beginnings, not endings.",
                ],
            },
        ],
        "facts": [
            "CRISPR makes targeted genetic edits using a guide RNA and a cutting enzyme.",
            "Germline edits are inherited and tightly restricted nearly everywhere.",
            "Biomanufacturing uses engineered cells as production factories.",
            "Falling sequencing and synthesis costs drive the field's progress.",
        ],
        "faq": [
            {
                "q": "Is gene editing the same as genetic modification?",
                "a": "Gene editing is a precise technique within the broader category of genetic modification. Editing usually changes existing DNA, while older modification often inserts genes from another organism.",
            },
            {
                "q": "Are gene-edited foods safe to eat?",
                "a": "Regulators assess each product individually. Several edited foods are approved in some markets, and scientific bodies generally assess them by the trait produced rather than the technique alone.",
            },
            {
                "q": "Can CRISPR cure diseases today?",
                "a": "A small number of gene-editing therapies are approved for specific conditions. Many more are in trials. Most common diseases involve multiple genes and are not yet addressable this way.",
            },
        ],
        "related": ["greentechnology", "artificialintelligence", "3dprinting"],
    },
    {
        "slug": "greentechnology",
        "name": "Green Technology",
        "short": "Green Tech",
        "icon": "🌱",
        "category": "Emerging",
        "title": "Green Technology: Clean Power and Efficiency",
        "meta": "What green technology covers, how renewables and storage work together, where efficiency gains come from, and the grid and materials problems still to solve.",
        "lede": "Green technology is engineering that reduces environmental impact, usually by replacing fossil energy, cutting waste or making materials and systems circular.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Green_technology",
        "keywords": ["green technology", "renewable energy", "energy storage", "sustainability", "clean tech", "circular economy"],
        "intro": [
            "Solar panels and wind turbines get the attention, but green technology is broader: batteries, heat pumps, efficient motors, low-carbon cement, recycling processes and software that reduces energy use in buildings and logistics.",
            "The shared measure is environmental benefit per unit of cost and carbon. That keeps the field honest, because a technology that needs more energy to build than it saves is not green.",
        ],
        "sections": [
            {
                "id": "generation",
                "h": "Clean generation and storage",
                "p": [
                    "Solar photovoltaics convert light directly into electricity and are now among the cheapest sources of new power in many regions. Wind is efficient at scale onshore and offshore, where capacity factors are higher and turbines larger.",
                    "Both are variable, so storage and flexibility matter. Lithium-ion batteries handle short shifts and fast frequency response, pumped hydro stores energy for longer, and grid interconnects move power between regions with different weather.",
                ],
                "list": [
                    "Solar PV: modular, fast to deploy, output depends on weather.",
                    "Wind: high output per turbine offshore, site-constrained onshore.",
                    "Batteries: fast response, falling cost, limited duration.",
                    "Pumped hydro and thermal storage: longer duration at scale.",
                    "Grids and interconnectors: the enabling infrastructure nobody photographs.",
                ],
            },
            {
                "id": "efficiency",
                "h": "Efficiency is the cheapest energy",
                "p": [
                    "Insulation, heat pumps, LED lighting and efficient motors reduce demand before any generation is built. For most buildings, cutting waste costs less per tonne of avoided carbon than adding new supply.",
                    "Software contributes quietly: better routing, cooling optimisation in data centres, and demand shifting that moves flexible loads to hours when clean power is abundant.",
                ],
            },
            {
                "id": "materials",
                "h": "Materials and circularity",
                "p": [
                    "Cement, steel and aluminium are hard to decarbonise because carbon is released by the chemistry, not just the fuel. Green hydrogen, electric furnaces and carbon capture are being tested at industrial scale.",
                    "Recycling is central but imperfect. Battery and solar recycling is improving, yet design for repair and disassembly matters more, because the greenest component is the one you do not have to make again.",
                ],
                "callout": "A grid powered by renewables, a building that needs less of it and a product designed to be repaired all beat a clever gadget that solves none of those.",
            },
            {
                "id": "barriers",
                "h": "The barriers that remain",
                "p": [
                    "Intermittency, permitting delays and grid connection queues now slow deployment more than technology cost in many markets. Supply chains for batteries and magnets are concentrated, and mining has its own environmental and social costs.",
                    "Storage economics beyond a few hours remain difficult, and heavy industry needs infrastructure that no single company can justify alone. Progress depends on policy, capital and patience as much as invention.",
                ],
            },
        ],
        "facts": [
            "Solar PV is among the cheapest new generation in many regions.",
            "Storage duration, not just capacity, decides grid reliability.",
            "Energy efficiency usually costs less than new generation per tonne avoided.",
            "Permitting and grid connections now bottleneck deployment.",
        ],
        "faq": [
            {
                "q": "Is green technology profitable?",
                "a": "Many segments are, especially solar, wind and efficiency services. Others, such as low-carbon cement or long-duration storage, still depend on policy support and scale.",
            },
            {
                "q": "Do electric vehicles really reduce emissions?",
                "a": "Yes over their lifetime in most grids, and the benefit grows as electricity decarbonises. Manufacturing, especially the battery, accounts for a significant share of lifetime emissions.",
            },
            {
                "q": "What is green hydrogen used for?",
                "a": "It is most useful where direct electrification is impractical, such as steelmaking, shipping fuel and long-term storage. Using it for home heating or cars is usually less efficient.",
            },
        ],
        "related": ["biotechnology", "semiconductors", "digitaltwins"],
    },
]
