# Content data for the Tech Topic guide pages (part 6).
# Each entry renders to /<slug> via scripts/build_topics.py.

TOPICS = [
    {
        "slug": "spatialcomputing",
        "name": "Spatial Computing",
        "short": "Spatial computing",
        "icon": "🥽",
        "category": "Emerging",
        "title": "Spatial Computing: How 3D Interfaces Actually Work",
        "meta": "A practical guide to spatial computing: how headsets track space, what passthrough and hand tracking can do, where the technology is useful today, and what still limits it.",
        "lede": "Spatial computing puts digital content into three-dimensional space and lets people interact with it using their hands, eyes and movement rather than a flat screen.",
        "image": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Spatial_computing",
        "keywords": ["spatial computing", "mixed reality", "AR VR", "headset tracking", "3D interface", "passthrough"],
        "intro": [
            "Spatial computing is an umbrella term for systems that understand and use physical space as part of the interface. A phone that places an arrow on a camera view, a headset that pins a browser window to your living-room wall and a pair of glasses that labels a machine on a factory floor are all doing the same core job: aligning digital content with the real world.",
            "The phrase became popular because virtual reality, augmented reality and mixed reality were converging. The interesting question is not which headset is best. It is whether the system can track where it is, where you are looking and what you are doing accurately enough for the task at hand.",
        ],
        "sections": [
            {
                "id": "tracking",
                "h": "How a headset knows where it is",
                "p": [
                    "Inside-out tracking uses cameras and inertial sensors on the device to build a map of the room and locate the headset within it. This is called simultaneous localisation and mapping, or SLAM. The same map lets the system keep a virtual object fixed in place when you walk around it.",
                    "Hand and eye tracking add the input layer. Cameras observe your hands, and infrared sensors estimate where your eyes are pointing. Eye tracking is useful for selection and foveated rendering, which draws full detail only where you are looking to save power.",
                ],
                "list": [
                    "Inertial measurement: fast but drifts over time.",
                    "Camera SLAM: accurate positioning and room mapping.",
                    "Depth sensing: better occlusion and object placement.",
                    "Hand and eye tracking: natural input without controllers.",
                ],
            },
            {
                "id": "passthrough",
                "h": "Passthrough, mixed reality and comfort",
                "p": [
                    "Passthrough cameras let a headset show the real world while drawing virtual objects on top. Latency and distortion decide whether the result feels solid or swims. Good mixed reality also needs occlusion, so a virtual ball can disappear behind a real chair.",
                    "Comfort remains the physical constraint. Weight, balance, heat and optical distortion cause fatigue. A device that is fine for a 20-minute demo can be unpleasant after an hour, which is why many productive use cases are short and task-specific.",
                ],
                "callout": "Spatial computing becomes useful when the 3D layer answers a question the physical world cannot answer on its own.",
            },
            {
                "id": "uses",
                "h": "Where it earns its place today",
                "p": [
                    "Training and simulation are the strongest cases. Trainees can practise a procedure, inspect a virtual engine or rehearse an emergency without consuming physical materials or risking safety. The value comes from repetition and measurement, not novelty.",
                    "Design review is another fit. Architects, engineers and product teams can walk through a model at scale and spot problems that a flat render hides. Remote assistance, where an expert annotates what a technician sees, is a smaller but practical market.",
                ],
            },
            {
                "id": "limits",
                "h": "What still holds it back",
                "p": [
                    "The hardware is only part of the problem. Content has to be built for 3D, interfaces have to be learned, and organisations need a reason to change a workflow that already works. A headset that replaces one monitor is a hard sell; one that replaces a training rig can be easy.",
                    "Privacy deserves attention too. Cameras and eye tracking collect intimate data about a room and a person. Clear retention rules, on-device processing and a visible recording indicator are baseline expectations, not premium features.",
                ],
            },
        ],
        "facts": [
            "Spatial computing aligns digital content with physical space.",
            "Inside-out tracking uses cameras and motion sensors, with no external base stations.",
            "Passthrough mixed reality needs low latency and occlusion to feel convincing.",
            "Training, design review and remote assistance are the clearest near-term uses.",
        ],
        "faq": [
            {
                "q": "Is spatial computing the same as virtual reality?",
                "a": "No. VR replaces your view with a virtual world. Spatial computing is broader and includes mixed and augmented reality, where digital content is placed into the real world. Most modern headsets support several modes.",
            },
            {
                "q": "Do I need a powerful PC for spatial computing?",
                "a": "Not always. Standalone headsets run applications on the device. PC-tethered systems are used for heavier rendering, simulation and professional design work.",
            },
            {
                "q": "Will spatial computing replace monitors?",
                "a": "For some focused workflows it can replace one or two screens, especially when travel or space is a constraint. For most office work, text clarity, comfort and battery life still favour a conventional display.",
            },
        ],
        "related": ["virtualreality", "augmentedreality", "wearabletechnology"],
    },
    {
        "slug": "autonomousvehicles",
        "name": "Autonomous Vehicles",
        "short": "Self-driving",
        "icon": "🚗",
        "category": "Emerging",
        "title": "Autonomous Vehicles: Sensors, Safety and the Road Ahead",
        "meta": "How self-driving cars perceive the road, what the levels of autonomy mean, why edge cases are hard, and where driverless services operate today.",
        "lede": "Autonomous vehicles combine sensors, maps and software to drive with less human involvement, but the hard part is proving safety in situations nobody anticipated.",
        "image": "https://images.unsplash.com/photo-1502877338535-766e1452684a?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Self-driving_car",
        "keywords": ["autonomous vehicles", "self-driving cars", "robotaxi", "LiDAR", "ADAS", "autonomy levels"],
        "intro": [
            "A self-driving car is a robot that has to work in public, at speed, around unpredictable people. The stack is a loop: sense the environment, build a model of what is happening, predict what other road users might do, plan a safe path and actuate the controls.",
            "The technology has split into two broad approaches. One relies on detailed maps and a rich sensor suite, often including LiDAR. The other leans on cameras and general-purpose perception, aiming to handle roads it has never seen. Both are trying to solve the same problem: the long tail of rare situations.",
        ],
        "sections": [
            {
                "id": "levels",
                "h": "What the levels of autonomy mean",
                "p": [
                    "The SAE scale runs from 0 to 5. At level 2 the driver must monitor the road while the car assists with steering and speed. At level 3 the system can handle parts of a trip but may ask the driver to take over. Level 4 can drive without a human inside a defined area, and level 5 is unrestricted autonomy.",
                    "The jump from 2 to 3 is awkward because the human is still a fallback but is no longer continuously engaged. If the system asks for help with seconds of warning, a distracted driver may not respond safely. That is why some manufacturers skip level 3 and target supervised or geofenced level 4 instead.",
                ],
                "list": [
                    "Level 0: warnings only.",
                    "Level 1-2: driver assistance, human monitors.",
                    "Level 3: conditional automation with fallback requests.",
                    "Level 4: driverless within a defined operational domain.",
                    "Level 5: unrestricted, still research.",
                ],
            },
            {
                "id": "sensors",
                "h": "Cameras, radar and LiDAR",
                "p": [
                    "Cameras are cheap, high-resolution and excellent at reading signs and lane markings, but they struggle in glare and darkness. Radar measures distance and velocity robustly in poor weather but has lower resolution. LiDAR builds a precise 3D point cloud, at a higher cost and with more moving parts on some designs.",
                    "Sensor fusion combines the strengths and cross-checks disagreements. The real work is calibration and redundancy: if one sensor is dirty, blinded or wrong, the system must know and degrade safely rather than confidently misunderstand the road.",
                ],
                "callout": "The safety argument is not that a car never makes a mistake. It is that its mistakes are rarer and less severe than a human baseline, across the roads it actually drives.",
            },
            {
                "id": "edge-cases",
                "h": "Why edge cases dominate",
                "p": [
                    "Most driving is routine. The remaining fraction includes temporary traffic lights, a mattress on the motorway, a cyclist signalling oddly or a construction worker waving you through. These situations are rare individually but common across a fleet, and they are exactly where hand-written rules break down.",
                    "Simulation helps by replaying rare events and generating variations at scale, but simulated miles are not the same as real ones. Validation needs a mix of closed-course testing, shadow driving, real supervised miles and transparent incident reporting.",
                ],
            },
            {
                "id": "today",
                "h": "What is actually on the road",
                "p": [
                    "Robotaxi services operate commercially in a handful of cities with defined areas and remote supervision. Driverless trucks are being tested on fixed routes. Consumer cars offer assisted driving that still requires an attentive driver, even when the marketing implies more.",
                    "The regulatory picture varies by country and even by city. Approval usually depends on the operational domain, the safety case, data recording and a plan for remote assistance. Expanding to a new city is a new engineering and regulatory project, not a toggle.",
                ],
            },
        ],
        "facts": [
            "Autonomy levels describe who is responsible for monitoring the road.",
            "Cameras, radar and LiDAR fail in different conditions, so fusion and redundancy matter.",
            "Rare edge cases, not routine driving, are the main obstacle to scale.",
            "Commercial driverless services are geofenced and remotely supervised.",
        ],
        "faq": [
            {
                "q": "Are self-driving cars legal?",
                "a": "It depends on the country and the operational domain. Some places allow commercial robotaxis in defined areas; others permit testing only. Consumer systems still require a licensed driver to monitor the road.",
            },
            {
                "q": "Do autonomous cars need LiDAR?",
                "a": "Not necessarily. Some companies build on cameras and radar, while others use LiDAR for precise depth. What matters is whether the sensor suite is reliable enough for the claimed operating conditions.",
            },
            {
                "q": "When will full autonomy arrive?",
                "a": "Unrestricted level 5 remains a research goal. Geofenced driverless services will keep expanding city by city, but a car that drives anywhere in any weather is not a near-term product.",
            },
        ],
        "related": ["robotics", "artificialintelligence", "5gnetworks"],
    },
    {
        "slug": "digitalidentity",
        "name": "Digital Identity",
        "short": "Digital ID",
        "icon": "🪪",
        "category": "Security",
        "title": "Digital Identity: How Online Identity Really Works",
        "meta": "Authentication, passkeys, digital wallets and identity verification explained: what proves who you are online, where the risks are, and how to protect an account.",
        "lede": "Digital identity is the set of credentials, devices and records that prove you are you online, and it is now the main battleground for account security.",
        "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Digital_identity",
        "keywords": ["digital identity", "authentication", "passkeys", "identity verification", "SSO", "digital wallet"],
        "intro": [
            "Every login is a small identity decision: is this person who they claim to be, and should they be allowed to do this? Most systems answer with three factors: something you know, something you have and something you are. The strength of a login comes from combining factors and reducing how much a stolen factor is worth.",
            "Digital identity is broader than passwords. It includes government-issued digital IDs, corporate single sign-on, social logins, device-bound passkeys and the verified attributes held in a digital wallet. The design question is always the same: who controls the credential, and what happens when it is lost or stolen?",
        ],
        "sections": [
            {
                "id": "authentication",
                "h": "From passwords to passkeys",
                "p": [
                    "Passwords are a shared secret, which means both the user and the service know them. That makes them phishable and reusable across breaches. Multi-factor authentication helps by adding a code or a hardware key, but one-time codes can still be relayed by a determined attacker.",
                    "Passkeys replace the shared secret with a cryptographic key pair. The private key stays on your device, protected by the device unlock, and the service stores only the public key. There is nothing reusable to phish, which is why passkeys are a meaningful improvement rather than another layer of friction.",
                ],
                "list": [
                    "Something you know: password or PIN.",
                    "Something you have: phone, security key or passkey.",
                    "Something you are: fingerprint or face.",
                    "Context: location, device and behaviour signals.",
                ],
            },
            {
                "id": "verification",
                "h": "Verification versus authentication",
                "p": [
                    "Authentication happens every time you sign in. Verification happens when a service checks a real-world attribute such as your age, address or right to work. Verification usually requires a document, a selfie or a database check, and it creates a privacy problem because the service may retain more than it needs.",
                    "Good systems separate the two. A site might verify your age once and then store only a yes/no claim, not your passport image. Reusable verified credentials, held in a wallet and shared selectively, aim to make that separation practical.",
                ],
                "callout": "The safest identity system collects the minimum, proves the claim and forgets the evidence.",
            },
            {
                "id": "wallets",
                "h": "Digital wallets and reusable credentials",
                "p": [
                    "A digital identity wallet stores signed credentials on a device and presents only the attributes a service requests. Instead of uploading a driving licence, you might prove that you are over 18 and live in a certain region. The signature lets the receiver trust the issuer without contacting them.",
                    "The model depends on standards, issuer trust and recovery. If a phone is lost, the credentials must be revocable and restorable. If an issuer is compromised, relying parties need a way to check revocation. These are operational problems, not just cryptography.",
                ],
            },
            {
                "id": "practical",
                "h": "Protecting your identity in practice",
                "p": [
                    "Turn on phishing-resistant multi-factor authentication, preferably a passkey or hardware key, for email, banking and work accounts. Email is the recovery channel for almost everything else, so it deserves the strongest protection you can use.",
                    "Reduce the number of places that hold your identity data. Use unique passwords in a manager, review app permissions, and be sceptical of any message that asks you to confirm a login you did not start. Recovery flows are a favourite target because they bypass the front door.",
                ],
            },
        ],
        "facts": [
            "Passkeys replace a shared secret with a device-bound cryptographic key.",
            "Verification checks attributes; authentication checks access.",
            "Data minimisation is a security control, not just a privacy preference.",
            "Email is the recovery channel for most accounts, so secure it first.",
        ],
        "faq": [
            {
                "q": "Are passkeys safer than passwords?",
                "a": "Yes, for phishing resistance and reuse. A passkey cannot be guessed or copied from a server breach, and it is bound to the site it was created for. Recovery still needs care, especially if all your devices are lost.",
            },
            {
                "q": "Is a digital ID the same as a login?",
                "a": "No. A digital ID proves attributes about you, such as your name or age. A login proves control of an account. Some systems combine them, but they are different jobs.",
            },
            {
                "q": "What should I do if my identity is stolen?",
                "a": "Secure your email and financial accounts first, change reused passwords, enable strong MFA, and contact the relevant providers. In many countries you can also place a fraud alert or freeze credit.",
            },
        ],
        "related": ["cybersecurity", "zerotrustsecurity", "blockchain"],
    },
    {
        "slug": "humanoidrobots",
        "name": "Humanoid Robots",
        "short": "Humanoids",
        "icon": "🤖",
        "category": "Emerging",
        "title": "Humanoid Robots: Why Two Legs Are So Hard",
        "meta": "How humanoid robots balance, see and manipulate objects, where they are being tested in warehouses and factories, and why general-purpose labour is still distant.",
        "lede": "Humanoid robots are built to work in spaces designed for people, which makes them flexible in theory and exceptionally difficult to make reliable in practice.",
        "image": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Humanoid_robot",
        "keywords": ["humanoid robots", "bipedal robots", "robot labour", "robot manipulation", "embodied AI", "robotics"],
        "intro": [
            "A humanoid robot is a machine with a torso, two arms, two legs and a head, designed to operate in environments built for humans. The appeal is obvious: factories, warehouses, labs and homes already have stairs, doors, shelves and tools sized for a person.",
            "The difficulty is equally obvious. Walking on two legs is a continuous balance problem, hands are complex, and every task happens in a world full of clutter. A robot that works in a demo is not the same as a robot that works for a shift without supervision.",
        ],
        "sections": [
            {
                "id": "body",
                "h": "Legs, hands and power",
                "p": [
                    "Bipedal locomotion needs fast sensing and control to keep the centre of mass over the support foot while moving. Electric actuators have improved enough for quiet, precise walking, but battery life and heat remain limiting. Many deployments use wheels for flat floors because they are simpler and more efficient.",
                    "Hands are the other hard part. A simple gripper is reliable for pick-and-place, while a multi-fingered hand can use human tools but needs tactile sensing and control that is still maturing. The useful question is what level of dexterity a task actually requires.",
                ],
                "list": [
                    "Actuators: electric motors with high torque density.",
                    "Balance: inertial sensors plus fast whole-body control.",
                    "Perception: cameras and depth sensors for objects and people.",
                    "Power: batteries that must last a useful shift.",
                ],
            },
            {
                "id": "control",
                "h": "From scripted motion to learned behaviour",
                "p": [
                    "Traditional robots repeat a carefully programmed path. Humanoids need to cope with variation: a box in a different position, a person crossing the aisle, a tool that slips. Modern approaches combine model-based control for balance with learned policies for perception and manipulation.",
                    "Teleoperation is a common bridge. A remote operator guides the robot through a task, and the resulting data trains a policy that can eventually run autonomously. This is practical but raises questions about how quickly the robot becomes independent and who is liable when it fails.",
                ],
                "callout": "A humanoid is a platform, not a product. Its value depends on the tasks it can reliably complete in a specific building.",
            },
            {
                "id": "work",
                "h": "Where humanoids are being tested",
                "p": [
                    "The first serious deployments are in structured industrial settings: moving totes, tending machines, inspecting equipment and handling repetitive material flow. These environments have predictable lighting, known layouts and a safety culture that can accommodate a new machine.",
                    "Homes are much harder. Homes are cluttered, people are unpredictable, and the tasks that matter are open-ended. A robot that folds one kind of laundry is impressive, but the economic case for a general household humanoid is not yet established.",
                ],
            },
            {
                "id": "economics",
                "h": "Safety, cost and the labour question",
                "p": [
                    "A humanoid that shares space with people needs force limiting, speed limits and reliable detection of humans. Standards for collaborative robots exist, but applying them to a walking machine in a busy warehouse is still new territory.",
                    "The economics depend on utilisation. An expensive robot that works one shift on one task may never pay back; one that can be redeployed across tasks improves the case. That flexibility is the entire promise, and it is also the hardest engineering problem.",
                ],
            },
        ],
        "facts": [
            "Humanoids are designed for environments built for people.",
            "Balance and dexterous hands are the core engineering constraints.",
            "Early deployments focus on structured industrial tasks, not homes.",
            "Utilisation across many tasks decides whether the economics work.",
        ],
        "faq": [
            {
                "q": "Are humanoid robots about to replace warehouse workers?",
                "a": "Not broadly. Current deployments are limited, supervised and task-specific. Labour shortages and dangerous tasks are the strongest near-term cases, but reliability and cost still constrain scale.",
            },
            {
                "q": "Why make a robot human-shaped at all?",
                "a": "Because the world is built for human bodies. Stairs, doors, shelves and tools already assume human reach and hands. A humanoid can, in principle, use the same infrastructure without rebuilding it.",
            },
            {
                "q": "Do humanoids use AI?",
                "a": "Increasingly, yes, especially for perception and manipulation. Balance and safety-critical control often remain model-based, with learned components layered on top.",
            },
        ],
        "related": ["robotics", "artificialintelligence", "wearabletechnology"],
    },
    {
        "slug": "datacenters",
        "name": "Data Centers",
        "short": "Data centers",
        "icon": "🏢",
        "category": "Infrastructure",
        "title": "Data Centers: Power, Cooling and the AI Boom",
        "meta": "How modern data centers are built, why AI workloads changed power and cooling, what happens to waste heat, and why siting has become a political decision.",
        "lede": "Data centers are factories for computation, and the AI boom has turned power, cooling and land into the binding constraints.",
        "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1200&h=630&fit=crop&auto=format",
        "wiki": "https://en.wikipedia.org/wiki/Data_center",
        "keywords": ["data centers", "AI infrastructure", "data center cooling", "power usage effectiveness", "hyperscale", "GPU clusters"],
        "intro": [
            "A data center is a building full of servers, storage and networking, designed to keep them powered, cool and connected. The cloud is not abstract: every region, bucket and model endpoint resolves to physical racks in a building with an electricity supply and a cooling system.",
            "The workload mix has shifted. Traditional web applications are relatively steady, while AI training clusters draw enormous power in bursts and produce intense heat in dense racks. That change is reshaping how data centers are designed, where they are built and how their environmental cost is measured.",
        ],
        "sections": [
            {
                "id": "anatomy",
                "h": "What is inside a data center",
                "p": [
                    "The white space holds racks of servers, storage arrays and network switches. Behind it sits the power chain: substations, transformers, uninterruptible power supplies, batteries and generators. Cooling is a separate system of chillers, air handlers or liquid loops.",
                    "Redundancy determines reliability. A tier classification describes how many independent paths exist for power and cooling. More redundancy means higher cost, which is why not every workload pays for the same level of resilience.",
                ],
                "list": [
                    "Compute and storage racks.",
                    "Power distribution and backup generation.",
                    "Cooling: air, evaporative or direct-to-chip liquid.",
                    "Networking: fibre routes and interconnection to carriers.",
                ],
            },
            {
                "id": "ai-power",
                "h": "Why AI changed the math",
                "p": [
                    "A rack of general-purpose servers might draw 5 to 15 kilowatts. A dense GPU rack for AI training can draw tens or even over a hundred kilowatts. Air cooling struggles at that density, so operators are moving to liquid cooling, including direct-to-chip plates and immersion systems.",
                    "Power is now the constraint that decides whether a site is viable. Grid connections can take years, and large campuses may need new substations. That is why operators sign long-term power contracts, invest in on-site generation and increasingly look at locations with available electricity.",
                ],
                "callout": "The cloud is limited by substations, water and land as much as by software.",
            },
            {
                "id": "efficiency",
                "h": "Measuring efficiency honestly",
                "p": [
                    "Power usage effectiveness compares total facility power with the power delivered to IT equipment. A PUE of 1.2 means 20 percent overhead. It is a useful ratio but a limited one: a facility can have excellent PUE and still consume enormous absolute energy.",
                    "Water use, carbon intensity and embodied emissions matter too. Evaporative cooling can be efficient with electricity but heavy on water. The honest comparison depends on the local grid, the climate and the workload, not a single headline number.",
                ],
            },
            {
                "id": "siting",
                "h": "Location, heat and the local bargain",
                "p": [
                    "Data centers are drawn to cheap land, reliable power, fibre connectivity and cool climates. But those advantages are increasingly contested. Local residents worry about noise, water use and grid capacity, while governments weigh tax incentives against energy demands.",
                    "Waste heat reuse is technically possible: district heating, greenhouses and industrial processes can absorb low-grade heat. The economics depend on proximity and a steady demand. It is a real option, but not a universal fix for the sector's energy footprint.",
                ],
            },
        ],
        "facts": [
            "AI racks can draw many times the power of traditional server racks.",
            "Liquid cooling is becoming necessary at high GPU densities.",
            "PUE measures overhead efficiency, not total environmental impact.",
            "Grid connections and local approval now gate new capacity.",
        ],
        "faq": [
            {
                "q": "Why do data centers use so much water?",
                "a": "Evaporative cooling removes heat by letting water evaporate, which is effective but consumes water. Operators can reduce it with air cooling, closed-loop liquid systems or reclaimed water, depending on climate and design.",
            },
            {
                "q": "What is PUE?",
                "a": "Power usage effectiveness is total facility power divided by IT equipment power. Lower is better, but it says nothing about how clean the electricity is or how much total power is used.",
            },
            {
                "q": "Can data centers be carbon neutral?",
                "a": "They can match electricity use with renewable generation and reduce emissions, but hardware manufacturing, backup generators and construction still produce emissions. Claims need a clear boundary and audited data.",
            },
        ],
        "related": ["cloudcomputing", "greentechnology", "semiconductors"],
    },
]
