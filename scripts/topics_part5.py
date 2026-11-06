# Content data for the Tech Topic guide pages (part 5).
# Newer topics are appended to the guide library without changing the existing
# entries in parts 1-4.

TOPICS = [
    {
        "slug": "augmentedreality",
        "name": "Augmented Reality",
        "short": "AR",
        "icon": "🕶️",
        "category": "Emerging",
        "title": "Augmented Reality Explained: AR Beyond the Hype",
        "meta": "A practical guide to augmented reality: how AR tracking works, where it is already useful, the difference from VR, and the hardware limits still holding it back.",
        "lede": "Augmented reality adds digital information to the world in front of you, using a phone, tablet or pair of glasses as the display.",
        "image": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Augmented_reality",
        "keywords": ["augmented reality", "what is AR", "AR glasses", "spatial computing", "AR vs VR", "augmented reality examples"],
        "intro": [
            "Augmented reality (AR) keeps you in the physical world and overlays digital content on top of it. The overlay might be a navigation arrow on a camera feed, a repair label attached to a machine, or a virtual sofa placed in your living room before you buy it.",
            "The technology has been through several hype cycles. What survived is a set of genuinely useful applications in maintenance, training, retail and navigation, plus a consumer market that is still waiting for glasses light and comfortable enough to wear all day.",
        ],
        "sections": [
            {
                "id": "how-ar-works",
                "h": "How AR knows where to put things",
                "p": [
                    "An AR system has to solve two problems at once: understand the scene and track its own position within it. Cameras, inertial sensors and sometimes depth sensors combine to estimate motion. Software detects planes, edges, markers or known images so virtual objects can be anchored to something stable.",
                    "Lighting is the next challenge. A virtual object that is brightly lit in a dim room looks pasted on. Modern engines estimate ambient light and add shadows, occlusion and reflections to make the composite convincing. The better the scene understanding, the less the brain has to work.",
                ],
                "list": [
                    "Marker-based AR: a printed code or image gives the system a precise anchor.",
                    "Markerless AR: plane and feature detection places objects without a printed target.",
                    "Location-based AR: GPS, compass and street data anchor content outdoors.",
                    "Wearable AR: glasses project images while leaving the real world visible.",
                ],
            },
            {
                "id": "where-ar-works",
                "h": "Where AR already earns its place",
                "p": [
                    "Industrial maintenance is one of the strongest cases. A technician can look at a machine and see the next step, the torque setting or the location of a hidden component without putting down tools to consult a manual. The same logic applies to assembly, inspection and remote expert support.",
                    "In retail, AR reduces uncertainty. Customers can preview furniture, paint, eyewear or footwear in context. In education, 3D models make abstract subjects tangible. In navigation, a live camera overlay can show which lane or doorway to take, though safety and battery use limit everyday adoption.",
                ],
                "callout": "The best AR applications remove a lookup or a guess. If the overlay does not save time or reduce errors, it is probably a demo rather than a product.",
            },
            {
                "id": "ar-limits",
                "h": "The limits worth knowing",
                "p": [
                    "Phones are the most widely available AR hardware, but holding a device up is tiring and narrows the field of view. Glasses solve that, but weight, battery life, heat, display brightness and social acceptability remain hard engineering trade-offs.",
                    "Privacy is the other constraint. A camera pointed at the world can capture faces, screens and private spaces. Products need clear recording indicators, on-device processing where possible and a convincing answer to who can access the data.",
                ],
            },
        ],
        "facts": [
            "AR overlays digital content on the real world; VR replaces the view entirely.",
            "Tracking and scene understanding are the core technical problems.",
            "Maintenance, training and retail previews are the clearest commercial uses.",
            "Comfortable all-day glasses remain the missing mass-market device.",
        ],
        "faq": [
            {
                "q": "Is AR the same as VR?",
                "a": "No. VR blocks out the real world and replaces it with a simulated one. AR keeps the real world visible and adds digital content to it. Mixed reality combines both by anchoring virtual objects in the physical space.",
            },
            {
                "q": "Do I need special glasses to use AR?",
                "a": "No. Most people already have an AR device in their pocket: a modern phone can track surfaces, place objects and run camera overlays. Glasses offer a hands-free experience but are not required.",
            },
            {
                "q": "What is spatial computing?",
                "a": "Spatial computing is a broader term for interfaces that understand and respond to physical space, including AR, VR and gesture or gaze control. It describes the interaction model rather than one specific device.",
            },
        ],
        "related": ["virtualreality", "artificialintelligence", "5gnetworks"],
    },
    {
        "slug": "drones",
        "name": "Drones & UAVs",
        "short": "Drones",
        "icon": "🛸",
        "category": "Emerging",
        "title": "Drones Explained: How UAVs Fly and Where They Work",
        "meta": "How drones fly, what separates a consumer quadcopter from an industrial UAV, and where inspection, mapping and delivery are genuinely useful.",
        "lede": "A drone is an aircraft without a pilot on board, controlled remotely or flown autonomously by onboard software.",
        "image": "https://images.unsplash.com/photo-1644088379091-d574269d422f?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Unmanned_aerial_vehicle",
        "keywords": ["drones", "UAV", "drone technology", "drone inspection", "drone mapping", "autonomous drones"],
        "intro": [
            "The word drone covers everything from a palm-sized toy to a fixed-wing aircraft that stays aloft for hours. What they share is a flight controller, sensors, a power source and a communications link. The expensive part is rarely the airframe; it is the payload, software and safety systems around it.",
            "Drones matter because they put a sensor where a person cannot easily stand: above a roof, inside a tunnel, over a field or in front of a wind turbine. The commercial value comes from cheaper inspection, faster mapping and less time spent in dangerous places.",
        ],
        "sections": [
            {
                "id": "flight",
                "h": "How a drone stays in the air",
                "p": [
                    "A multirotor uses several rotors to generate lift and change direction by varying their speed. The flight controller reads accelerometers, gyroscopes, barometers and often GPS, then makes hundreds of tiny corrections per second. Without that loop, a quadcopter would be almost impossible for a person to fly manually.",
                    "Fixed-wing drones trade hover capability for range and efficiency. Hybrid designs tilt rotors or use a wing plus lift fans. The right choice depends on whether the job needs to hover precisely, cover distance quickly or carry a heavy payload.",
                ],
                "list": [
                    "Flight controller: the stabilisation and navigation brain.",
                    "IMU: accelerometers and gyroscopes that measure motion.",
                    "GNSS: satellite positioning for routes and return-to-home.",
                    "Payload: camera, thermal sensor, lidar, sprayer or delivery box.",
                    "Data link: radio control and video, with fail-safes for loss of signal.",
                ],
            },
            {
                "id": "uses",
                "h": "Where drones are actually deployed",
                "p": [
                    "Infrastructure inspection is the largest serious market. Power lines, bridges, cell towers, pipelines and wind turbines can be examined with a camera or thermal sensor while the asset keeps running. The drone does not replace the engineer; it gives the engineer a better viewpoint with less scaffolding and less risk.",
                    "Surveying and agriculture use photogrammetry and multispectral cameras to build maps, measure volumes and spot crop stress. Delivery remains promising but constrained by payload, weather, airspace rules and the cost of the last hundred metres. Emergency services use drones for search, fire mapping and situational awareness.",
                ],
                "callout": "The durable drone business is not flying. It is turning a difficult inspection into a repeatable, auditable data product.",
            },
            {
                "id": "rules",
                "h": "Safety, airspace and privacy",
                "p": [
                    "Drones share airspace with aircraft, people and property. Most countries set altitude limits, require visual line of sight, restrict flights near airports and sensitive sites, and demand registration above a weight threshold. Remote ID and geofencing are becoming standard safety features.",
                    "Privacy is a design issue as much as a legal one. A camera drone can capture neighbours, workers or private property without obvious consent. Responsible operators publish flight policies, minimise retention and avoid flying where there is no legitimate reason to be.",
                ],
            },
        ],
        "facts": [
            "A flight controller makes constant corrections that humans cannot match manually.",
            "Inspection and mapping are more mature markets than consumer delivery.",
            "Fixed-wing drones trade hovering for range and efficiency.",
            "Airspace rules and privacy obligations vary sharply by country.",
        ],
        "faq": [
            {
                "q": "Do you need a licence to fly a drone?",
                "a": "It depends on the country, the drone's weight and how it is used. Many places allow recreational flights under a threshold with registration, while commercial or heavier operations need a licence and insurance. Check the local aviation authority before flying.",
            },
            {
                "q": "How long can a drone stay in the air?",
                "a": "Consumer quadcopters typically fly for 20 to 40 minutes. Fixed-wing and hybrid industrial drones can stay up for hours, but payload, wind and battery reserve reduce the practical figure.",
            },
            {
                "q": "Are delivery drones practical yet?",
                "a": "In selected areas they work for small, light parcels, but weather, airspace, noise, payload limits and the cost of the final handoff keep them niche. They are usually one part of a delivery network, not a replacement for it.",
            },
        ],
        "related": ["robotics", "edgecomputing", "5gnetworks"],
    },
    {
        "slug": "nanotechnology",
        "name": "Nanotechnology",
        "short": "Nanotech",
        "icon": "⚛️",
        "category": "Emerging",
        "title": "Nanotechnology: Engineering the Very Small",
        "meta": "What nanotechnology really means, how materials behave differently at the nanoscale, and where medicine, chips and clean energy are using it today.",
        "lede": "Nanotechnology engineers matter at the scale of atoms and molecules, where familiar materials can behave in unfamiliar ways.",
        "image": "https://images.unsplash.com/photo-1782155789465-9bae14cbfba5?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Nanotechnology",
        "keywords": ["nanotechnology", "nanomaterials", "nanoscale", "molecular engineering", "nanomedicine", "semiconductor manufacturing"],
        "intro": [
            "Nanotechnology is not one product. It is a set of techniques for making and controlling structures between roughly one and one hundred nanometres across. At that scale, a material's surface area, colour, strength, conductivity and chemical reactivity can change dramatically without changing its chemical formula.",
            "That is why the field spans drug delivery, chip fabrication, water filtration, batteries, coatings and sensors. The common thread is precision: arranging matter so that a useful property emerges from the structure rather than from bulk chemistry alone.",
        ],
        "sections": [
            {
                "id": "why-size-matters",
                "h": "Why size changes the rules",
                "p": [
                    "As a particle gets smaller, a larger fraction of its atoms sit at the surface. Surface atoms have fewer neighbours and more unsatisfied bonds, which makes nanoparticles chemically active and useful for catalysis, sensing and antimicrobial surfaces. It can also make them toxic or hard to handle.",
                    "Quantum effects appear when structures are small enough to confine electrons. Quantum dots, for example, emit different colours depending on their size. This is already used in displays and biological imaging, and it is a reminder that nanoscale engineering is not simply miniaturisation.",
                ],
                "list": [
                    "High surface area: more reactive, useful for catalysts and filters.",
                    "Quantum confinement: size determines colour and electronic behaviour.",
                    "Self-assembly: molecules arrange themselves into useful structures.",
                    "Bottom-up fabrication: build from molecules rather than carve from bulk.",
                ],
            },
            {
                "id": "applications",
                "h": "Where it is already working",
                "p": [
                    "Semiconductor manufacturing is the most economically important example. Modern chips are patterned at nanometre dimensions, and advances in lithography, deposition and etching are applied nanoscience at industrial scale. Without it, the last several generations of processors would not exist.",
                    "In medicine, lipid nanoparticles carry mRNA vaccines, while targeted nanoparticles are being studied for delivering chemotherapy with fewer side effects. In energy, nanostructured electrodes improve battery charging and catalysts improve fuel cells. Water treatment uses nanomaterials to adsorb contaminants or kill microbes.",
                ],
                "callout": "The most important nanotechnology is often invisible: it is a manufacturing step inside a chip or a battery, not a miracle material with a label.",
            },
            {
                "id": "risks",
                "h": "The safety and governance questions",
                "p": [
                    "A nanomaterial can be more hazardous than the same substance in bulk because it can penetrate cells or travel further in the body. Risk assessment has to consider size, shape, surface chemistry, dose and how the material is bound or contained.",
                    "Regulation is fragmented across chemicals, medicines, food and workplace safety. Good practice means testing the specific nanomaterial rather than assuming the bulk substance's safety data applies, and designing containment into manufacturing from the start.",
                ],
            },
        ],
        "facts": [
            "The nanoscale is roughly 1 to 100 nanometres, where surface effects dominate.",
            "Chip fabrication is the largest industrial application of nanoscale engineering.",
            "Lipid nanoparticles made mRNA vaccines practical at scale.",
            "Nanomaterials need their own safety testing, not just bulk-material data.",
        ],
        "faq": [
            {
                "q": "Is nanotechnology already in everyday products?",
                "a": "Yes. It appears in chip manufacturing, sunscreens, stain-resistant coatings, batteries, water filters and some medicines. The label is less visible than the technology.",
            },
            {
                "q": "Is nanotechnology dangerous?",
                "a": "Some nanomaterials carry risks because their small size and high surface area change how they interact with living systems. The risk depends on the material, its form and how it is used. Regulation and containment matter.",
            },
            {
                "q": "What is the difference between nanotechnology and molecular manufacturing?",
                "a": "Nanotechnology is the broad practice of engineering at the nanoscale. Molecular manufacturing is a more specific and still largely theoretical vision of building objects atom by atom with molecular machines.",
            },
        ],
        "related": ["semiconductors", "biotechnology", "greentechnology"],
    },
    {
        "slug": "spacetechnology",
        "name": "Space Technology",
        "short": "Space",
        "icon": "🚀",
        "category": "Emerging",
        "title": "Space Technology Explained: Reuse and Access",
        "meta": "How satellites, reusable rockets and cheap launch are changing space technology, from Earth observation and broadband to navigation and scientific research.",
        "lede": "Space technology covers the rockets, satellites and ground systems that let us observe Earth, communicate across it and explore beyond it.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Outline_of_spaceflight",
        "keywords": ["space technology", "satellites", "reusable rockets", "Earth observation", "satellite internet", "space industry"],
        "intro": [
            "Space used to be a government-only enterprise measured in decades and national budgets. Lower launch costs, smaller satellites and commercial launch providers changed the economics. A university or startup can now put a small payload into orbit for a fraction of what it cost a generation ago.",
            "The result is a growing layer of infrastructure around Earth: cameras that monitor crops and disasters, radios that connect remote regions, clocks that underpin navigation, and sensors that track weather and climate. Space technology is increasingly something we depend on rather than only something we admire.",
        ],
        "sections": [
            {
                "id": "launch",
                "h": "Why launch is the bottleneck",
                "p": [
                    "Getting to orbit requires enormous energy. A rocket has to accelerate to roughly 7.8 kilometres per second, and most of its mass at liftoff is propellant. Reusability helps by amortising the cost of the booster across many flights, but refurbishment, inspection and range operations still dominate the economics.",
                    "Small launchers serve dedicated orbits for small satellites, while rideshare missions spread the cost across many customers. The trade-off is schedule and orbital flexibility against price. Launch is not the only cost: ground stations, insurance, licensing and operations often exceed the hardware budget.",
                ],
                "list": [
                    "Expendable launch: the rocket is used once.",
                    "Reusable launch: boosters return for refurbishment and reuse.",
                    "Rideshare: many small payloads share one launch.",
                    "Orbital transfer: a space tug moves payloads between orbits.",
                ],
            },
            {
                "id": "satellites",
                "h": "What satellites actually do",
                "p": [
                    "Communications satellites relay signals between ground stations, extending broadband and broadcasting. Earth-observation satellites image the surface in visible, infrared or radar bands, supporting agriculture, forestry, disaster response and defence. Navigation constellations broadcast timing signals that phones use to calculate position.",
                    "Low Earth orbit has become the busy layer. Closer orbits reduce latency for internet services and improve image resolution, but they require large constellations and careful collision avoidance. Space debris and radio spectrum are shared resources, which makes coordination a technical and political problem.",
                ],
                "callout": "The value of a satellite is not the spacecraft. It is the data, connectivity or timing signal that reaches a customer on the ground.",
            },
            {
                "id": "access",
                "h": "The new access economy",
                "p": [
                    "Standardised small-satellite buses, off-the-shelf components and hosted payloads have lowered the barrier to entry. Companies can buy a ride, plug in a sensor and focus on the application rather than building a spacecraft from scratch.",
                    "At the same time, the most valuable services depend on ground infrastructure: antennas, cloud processing and distribution rights. Space is becoming a data business with a hardware problem at the edge, not a pure aerospace business.",
                ],
            },
        ],
        "facts": [
            "Orbital velocity is about 7.8 km/s, which is why launch is so energy-intensive.",
            "Reusability reduces hardware cost but adds refurbishment and inspection work.",
            "Earth observation, broadband and navigation are the largest commercial segments.",
            "Space debris and spectrum coordination are shared-resource problems.",
        ],
        "faq": [
            {
                "q": "Why are reusable rockets important?",
                "a": "They can spread the cost of a booster across multiple launches and increase flight cadence. The savings depend on how quickly and cheaply the vehicle can be inspected and refurbished.",
            },
            {
                "q": "What is the difference between LEO and GEO?",
                "a": "Low Earth orbit is a few hundred to a couple of thousand kilometres up, giving lower latency but requiring constellations for continuous coverage. Geostationary orbit is about 35,786 kilometres up, where a satellite matches Earth's rotation and stays over one point.",
            },
            {
                "q": "Is satellite internet a replacement for fibre?",
                "a": "It is a complement, especially in rural, maritime and emergency settings. Fibre still offers far more capacity per user in dense areas; satellite systems are best where terrestrial infrastructure is absent or unreliable.",
            },
        ],
        "related": ["5gnetworks", "robotics", "semiconductors"],
    },
    {
        "slug": "wearabletechnology",
        "name": "Wearable Technology",
        "short": "Wearables",
        "icon": "⌚",
        "category": "Hardware",
        "title": "Wearables: Health, AR and Ambient Computing",
        "meta": "How wearables measure the body, why health sensors are becoming more capable, and what smart glasses and rings mean for privacy and everyday computing.",
        "lede": "Wearables put sensors and computation on the body, turning continuous movement, heart rate and context into useful signals.",
        "image": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Wearable_technology",
        "keywords": ["wearable technology", "smartwatch", "fitness tracker", "smart ring", "smart glasses", "health sensors"],
        "intro": [
            "A wearable is a computer you keep on your body rather than take out of a pocket. That sounds like a small distinction, but it changes what the device can measure: continuous heart rate, movement, sleep, temperature, blood oxygen and the context of being somewhere.",
            "The category includes watches, rings, glasses, hearables and even clothing. The successful products tend to do one job reliably and disappear into a routine. The failures tend to ask for attention without giving much back.",
        ],
        "sections": [
            {
                "id": "sensors",
                "h": "What a wearable can measure",
                "p": [
                    "Optical sensors shine light into the skin and measure how much is absorbed to estimate heart rate and blood oxygen. Accelerometers and gyroscopes detect movement and posture. Some devices add temperature, electrodermal activity or electrical signals from the heart.",
                    "The hard part is not collecting a signal; it is making it meaningful. Motion, skin tone, fit and ambient light all affect accuracy. A raw optical reading is not a medical diagnosis, and products need to communicate uncertainty rather than present every number as fact.",
                ],
                "list": [
                    "Photoplethysmography: light-based heart-rate and oxygen sensing.",
                    "Accelerometer: step counting, sleep staging and fall detection.",
                    "Temperature: fever trends, cycle tracking and recovery signals.",
                    "GPS: routes, pace and outdoor activity context.",
                ],
            },
            {
                "id": "form-factors",
                "h": "Watches, rings and glasses",
                "p": [
                    "A watch has the most room for a display, battery and sensors, which makes it the default health wearable. A ring is smaller and less intrusive, often with better sleep comfort, but it has fewer controls and less space for a battery. Glasses can show information in the user's field of view, but weight and social acceptance remain difficult.",
                    "Hearables are an underrated category. Earbuds already sit in a stable position, have batteries and can measure movement, temperature and sound. The challenge is making new sensors useful without turning every pair of earbuds into a medical device.",
                ],
            },
            {
                "id": "privacy",
                "h": "The privacy bargain",
                "p": [
                    "Wearables collect intimate data continuously: sleep, fertility, stress, location and exercise. That data can be valuable to the user and to insurers, employers, advertisers and data brokers. The user needs clear control over export, deletion and third-party access.",
                    "Health claims deserve scrutiny. A feature that estimates recovery or detects an irregular rhythm is not the same as a diagnosis. Good products explain the evidence, the false-positive rate and when to see a clinician.",
                ],
                "callout": "A wearable earns trust by being boring about data: collect less, explain more, and make deletion easy.",
            },
        ],
        "facts": [
            "Continuous body sensing is what separates wearables from phones.",
            "Optical heart-rate sensors are affected by motion, fit and skin tone.",
            "Rings trade display and controls for comfort and sleep tracking.",
            "Health data is among the most sensitive personal data a product can hold.",
        ],
        "faq": [
            {
                "q": "Are wearable health sensors accurate enough to rely on?",
                "a": "They are useful for trends and general awareness, but they are not a substitute for clinical testing. Accuracy varies by sensor, fit and activity. Treat alerts as a prompt to seek professional advice, not as a diagnosis.",
            },
            {
                "q": "Do smart rings work as well as smartwatches?",
                "a": "Rings can be excellent for sleep and recovery because they are comfortable, but they have fewer controls and less space for sensors. Watches are better for workouts, notifications and GPS.",
            },
            {
                "q": "What should I check before buying a wearable?",
                "a": "Look at sensor accuracy, battery life, comfort, data export, privacy policy and whether the features you want require a subscription. A device that fits your routine beats one with a longer spec sheet.",
            },
        ],
        "related": ["internetofthings", "virtualreality", "artificialintelligence"],
    },
    {
        "slug": "smartcities",
        "name": "Smart Cities",
        "short": "Smart cities",
        "icon": "🏙️",
        "category": "Emerging",
        "title": "Smart Cities: Sensors, Data and Public Trust",
        "meta": "What makes a city smart: connected infrastructure, digital twins, mobility data and the governance questions that decide whether residents trust it.",
        "lede": "A smart city uses data and connected infrastructure to run services more efficiently, but the hard part is governance rather than technology.",
        "image": "https://images.unsplash.com/photo-1758073519996-6d3c63b4922c?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Smart_city",
        "keywords": ["smart cities", "urban technology", "city sensors", "digital twin city", "smart mobility", "public data"],
        "intro": [
            "Cities are systems of systems: transport, water, power, waste, housing and emergency services all interact. Smart-city projects try to instrument those systems, share data between them and use the result to make better decisions.",
            "The technology is often less difficult than the politics. A sensor network can measure air quality, but it cannot decide who owns the data, who is accountable when an algorithm is wrong, or whether residents were consulted. Those questions determine whether a project is useful or merely well-funded.",
        ],
        "sections": [
            {
                "id": "layers",
                "h": "The layers of a smart city",
                "p": [
                    "The first layer is sensing: cameras, air-quality monitors, parking sensors, smart meters and vehicle telemetry. The second is connectivity, usually a mix of fibre, cellular and low-power radio. The third is a data platform that normalises and shares information across departments.",
                    "The final layer is action: dynamic traffic signals, predictive maintenance, emergency response and public dashboards. Value appears when data crosses a departmental boundary, which is exactly where procurement, privacy and ownership conflicts tend to appear.",
                ],
                "list": [
                    "Sensing: what is happening in the physical city.",
                    "Connectivity: moving data reliably and securely.",
                    "Platform: common standards, identity and access control.",
                    "Action: operational decisions and public services.",
                ],
            },
            {
                "id": "mobility",
                "h": "Mobility and digital twins",
                "p": [
                    "Transport is the most visible use case. Real-time vehicle and passenger data can adjust signals, prioritise buses, guide drivers to available parking and help planners model a new cycle lane before building it. The risk is optimising for cars because cars are easiest to measure.",
                    "A digital twin is a live model of a physical system, such as a district, a water network or a transit corridor. It lets planners test scenarios and operators diagnose failures. A twin is only as good as its data and its assumptions; a beautiful 3D model with stale inputs is a presentation, not a tool.",
                ],
                "callout": "A smart city is not a vendor product. It is a governance commitment to share data, measure outcomes and let residents see the evidence.",
            },
            {
                "id": "trust",
                "h": "Privacy, equity and accountability",
                "p": [
                    "Urban sensors can reveal where people live, work and gather. Cameras raise surveillance concerns, and algorithmic decisions about policing, housing or benefits can encode bias. Privacy impact assessments, data minimisation and independent oversight are not optional extras.",
                    "Equity matters too. A service that only works for people with a smartphone excludes those without one. Good projects keep analog channels open, publish performance data and give residents a way to challenge automated decisions.",
                ],
            },
        ],
        "facts": [
            "Smart-city value comes from integrating data across departments.",
            "Transport and infrastructure maintenance are the most common starting points.",
            "Digital twins are only useful when their data is current and governed.",
            "Privacy, equity and accountability decide public trust.",
        ],
        "faq": [
            {
                "q": "What is a digital twin in a city?",
                "a": "It is a live virtual model of a physical system, fed by sensor and operational data. Planners use it to simulate changes, and operators use it to detect and diagnose problems.",
            },
            {
                "q": "Are smart cities just surveillance cities?",
                "a": "They can become that if data collection is broad, opaque and unaccountable. The alternative is purpose-limited sensing, clear retention rules, independent oversight and public reporting.",
            },
            {
                "q": "What is a realistic first smart-city project?",
                "a": "Start with a narrow operational problem, such as streetlight energy use, water leakage or bus reliability. Instrument it, publish the baseline and measure whether the intervention improved the outcome.",
            },
        ],
        "related": ["internetofthings", "edgecomputing", "cybersecurity"],
    },
]
