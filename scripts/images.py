#!/usr/bin/env python3
"""Curated Unsplash imagery for Digital Infohub.

One registry powers:
  * social share images (og:image / twitter:image) on every page
  * the "Technology, in focus" clickable cards injected across the site
  * the subtle ambient background behind each page

Every entry below is a real, free Unsplash (images.unsplash.com) photo that
was checked against its Unsplash page before being added. Each photo is mapped
to the pages it genuinely describes; generic filler was removed.

Do not hand-write image URLs elsewhere — add them here.
"""
from html import escape

SHARE_W, SHARE_H = 1200, 630
CARD_W, CARD_H = 640, 400
AMBIENT_W, AMBIENT_H = 1200, 675


def _photo_url(photo_id: str, w: int, h: int, q: int = 80) -> str:
    return (
        f"https://images.unsplash.com/{photo_id}"
        f"?w={w}&h={h}&fit=crop&auto=format&q={q}"
    )


def _img(id, photo, tag, title, blurb, href, cta, alt):
    return {
        "id": id, "photo": photo, "tag": tag, "title": title,
        "blurb": blurb, "href": href, "cta": cta, "alt": alt,
    }


IMAGES = [
    _img("ai-chip", "photo-1697577418970-95d99b5a55cf", "Artificial intelligence",
         "AI, in one chip",
         "A modern AI accelerator is a city of transistors built to multiply matrices. That is why chip supply, power and cooling decide who can train the biggest models.",
         "/artificialintelligence", "Read the AI guide",
         "Microchip stamped with the letter A, representing an AI processor"),
    _img("brain", "photo-1677442135703-1787eea5ce01", "Machine learning",
         "The shape of a model",
         "A model is a structure plus millions of tuned numbers. Change the data or the evaluation and you get a different product, not just a different score.",
         "/machinelearning", "Read the machine learning guide",
         "Circuit board shaped like a glowing brain"),
    _img("quantum", "photo-1681908571122-97f349e1ace0", "Quantum computing",
         "Computing with qubits",
         "Quantum hardware is a physics experiment you can program. Error correction, not raw qubit count, is the number that decides when it becomes useful.",
         "/quantumcomputing", "Read the quantum guide",
         "Quantum computer with gold plates and silver wiring"),
    _img("server", "photo-1695668548342-c0c1ad479aee", "Data centres",
         "The building behind the cloud",
         "Cloud regions are physical campuses full of power, cooling and fibre. That geography explains latency, cost and most data-sovereignty rules.",
         "/datacenters", "Read the data centre guide",
         "Rack of servers in a data centre"),
    _img("cloud-room", "photo-1564457461758-8ff96e439e83", "Cloud",
         "Rent the computer, keep the control",
         "Cloud computing turns capital spending into a monthly bill. The trade is flexibility for a dependency you have to manage deliberately.",
         "/cloudcomputing", "Read the cloud guide",
         "Server room with rows of cabinets and blue cabling"),
    _img("serverless", "photo-1667984390538-3dea7a3fe33d", "Serverless",
         "Servers you never see",
         "Serverless moves the machine out of your mental model. You pay per request and the platform handles scaling, cold starts and the bill you forgot to cap.",
         "/serverlesscomputing", "Read the serverless guide",
         "Three-dimensional cloud computing illustration"),
    _img("security", "photo-1550751827-4bd374c3f58b", "Cybersecurity",
         "Security starts with identity",
         "Most breaches begin with a stolen session or a weak credential, not a broken firewall. Strong identity checks and short-lived access do more than another perimeter tool.",
         "/cybersecurity", "Read the security guide",
         "Close-up of a secure processor on a circuit board"),
    _img("padlock", "photo-1555529902-5261145633bf", "Privacy",
         "Your data, your rules",
         "Privacy is a product decision, not a policy page. Collect less, keep it for less time and explain plainly what leaves the device.",
         "/privacy-policy", "Read the privacy policy",
         "Silver padlock on a dark surface"),
    _img("lock-keyboard", "photo-1633265486064-086b219458ec", "Passwords",
         "Long beats complicated",
         "A long passphrase is easier to remember and harder to crack than a short tangle of symbols. A password manager removes the guesswork entirely.",
         "/software/password", "Open the password generator",
         "Golden padlock resting on a computer keyboard"),
    _img("iot", "photo-1558002038-1055907df827", "IoT",
         "Connected by default",
         "A modern home runs more connected sensors than laptops. The value is in the data, but every new endpoint is also a new door to defend.",
         "/internetofthings", "Read the IoT guide",
         "Phone used as a smart-home key at a front door"),
    _img("dashboard", "photo-1666875753105-c63a6f3bdc86", "Big data",
         "Finding signal in the noise",
         "Data teams spend more time cleaning and labelling than modelling. The quality of that groundwork decides whether a dashboard is trusted or ignored.",
         "/bigdata", "Read the big data guide",
         "Analytics dashboard with charts on a screen"),
    _img("chart", "photo-1611974789855-9c2a0a7236a3", "Markets",
         "Prices are a story, not a score",
         "A chart shows what happened, not why. Rates, earnings and risk appetite explain more than any single candle on a screen.",
         "/coincompass", "Open CoinCompass",
         "Stock market candlestick chart on a dark screen"),
    _img("bitcoin", "photo-1623227413711-25ee4388dae3", "Web3",
         "Ownership, without a middleman",
         "Public blockchains let strangers agree on a record without a referee. That is powerful for settlement and provenance, and unnecessary for most databases.",
         "/web3", "Read the Web3 guide",
         "Physical bitcoin token resting on gold nuggets"),
    _img("cubes", "photo-1639322537228-f710d846310a", "Blockchain",
         "Blocks, ledgers and trust",
         "A blockchain is a shared record no single party can quietly rewrite. Useful for settlement and provenance; overkill for a shopping list.",
         "/blockchain", "Read the blockchain guide",
         "Glowing translucent cubes arranged in a chain"),
    _img("microchip", "photo-1782155789465-8acb598726e1", "Hardware",
         "Inside the silicon bottleneck",
         "A leading-edge chip takes months to fabricate and thousands of steps to test. That complexity is why capacity became a strategic asset.",
         "/semiconductors", "Read the semiconductor guide",
         "Illuminated microchip on a dark circuit board"),
    _img("circuit", "photo-1782155789465-9bae14cbfba5", "Semiconductors",
         "The machine that makes machines",
         "Lithography, deposition and packaging are the unglamorous steps that turn a design into silicon. Each one is a global supply chain in miniature.",
         "/semiconductors", "Read the semiconductor guide",
         "Macro photograph of a dense electronic circuit board"),
    _img("robot-arm", "photo-1655393001768-d946c97d6fd1", "Robotics",
         "Robots do the dull, dirty and dangerous",
         "Industrial arms repeat a precise motion millions of times. The value is reliability and uptime, not human-like intelligence.",
         "/robotics", "Read the robotics guide",
         "White robotic arm in a display showroom"),
    _img("humanoid", "photo-1593376853899-fbb47a057fa0", "Humanoid robots",
         "Why build a robot that looks like us?",
         "A humanoid shape lets a machine use stairs, tools and doorways built for people. It also makes every balance problem much harder.",
         "/humanoidrobots", "Read the humanoid robots guide",
         "Humanoid robot waving in a bright modern building"),
    _img("drone", "photo-1473968512647-3e447244af8f", "Drones",
         "A sensor where a person cannot stand",
         "Drones put a camera above a roof, inside a tunnel or over a field. The business is the repeatable inspection data, not the flying.",
         "/drones", "Read the drone guide",
         "Drone flying against a clear sky"),
    _img("tesla", "photo-1491921125492-f0b9c835b699", "Autonomous vehicles",
         "The hard part is the edge case",
         "Self-driving progress is measured in rare events, not average miles. Sensors, maps and fallback drivers all exist because the last percent is hard.",
         "/autonomousvehicles", "Read the autonomous vehicles guide",
         "Interior view of a Tesla car dashboard"),
    _img("tower", "photo-1602823284936-463177448097", "5G & networks",
         "Networks that think",
         "Modern networks do not just move packets; they schedule workloads, slice bandwidth and push compute closer to users. That is what makes low-latency apps feel instant.",
         "/5gnetworks", "Explore 5G networks",
         "Black telecommunications tower against a blue sky"),
    _img("fiber", "photo-1604869515882-4d10fa4b0492", "Edge computing",
         "Designed for the edge",
         "Processing data near the device cuts round trips and bandwidth bills. It also creates a fleet of small systems that must be updated and secured remotely.",
         "/edgecomputing", "Read the edge guide",
         "Blue and white light trails representing a fibre network"),
    _img("vr", "photo-1783095593983-7936ec02f205", "VR & AR",
         "The next interface",
         "VR and AR are finding real work in training, design review and simulation. The hardware is improving faster than the comfort and content problems.",
         "/virtualreality", "Read the VR guide",
         "Person wearing a virtual reality headset on a platform"),
    _img("watch", "photo-1579586337278-3befd40fd17a", "Wearables",
         "A computer on your wrist",
         "Wearables succeed when they measure something you would not otherwise notice, then get out of the way. Battery life is the real feature.",
         "/wearabletechnology", "Read the wearables guide",
         "Smartwatch with a colourful app display"),
    _img("fruit-watch", "photo-1434494878577-86c23bcb06b9", "Wearables",
         "Health tracking that sticks",
         "The useful wearable is the one you forget you are wearing. Continuous heart, sleep and movement data only matters if the habit lasts.",
         "/post/newest-apple-watch-2026", "Read the Apple Watch guide",
         "Person checking an Apple Watch on their wrist"),
    _img("printer", "photo-1758435170505-e9b2772348c1", "3D printing",
         "From idea to prototype",
         "Additive manufacturing turns a CAD file into a physical part in hours. It is best for complex geometry, small batches and parts that would be costly to machine.",
         "/3dprinting", "Read the 3D printing guide",
         "3D printer with orange accents on a workbench"),
    _img("cells", "photo-1576086213369-97a306d36557", "Biotechnology",
         "Biology is becoming engineering",
         "Gene editing, lab-grown tissue and cheap sequencing turn biology into a design discipline. The hard limits are still safety, regulation and biology itself.",
         "/biotechnology", "Read the biotech guide",
         "Microscopic view of purple cells"),
    _img("microscope", "photo-1614308460927-5024ba2e1dcb", "Nanotechnology",
         "Working at the scale of atoms",
         "At the nanoscale, materials behave differently. That is the promise and the problem: new properties also mean new unknowns.",
         "/nanotechnology", "Read the nanotechnology guide",
         "Laboratory microscope with objective lenses"),
    _img("wind", "photo-1548337138-e87d889cc369", "Green tech",
         "Clean power needs a grid to match",
         "Solar and wind are cheap to build and intermittent to run. Storage, transmission and demand flexibility are the real engineering problems.",
         "/greentechnology", "Read the green tech guide",
         "White wind turbine standing in a field"),
    _img("city", "photo-1477959858617-67f85cf4f1df", "Smart cities",
         "Cities are systems, not gadgets",
         "A smart city joins transport, power, water and planning data. The wins come from operations, not from another app for residents.",
         "/smartcities", "Read the smart cities guide",
         "Dense city skyline seen from above"),
    _img("model3d", "photo-1622737133809-d95047b9e673", "Digital twins",
         "A copy that earns its keep",
         "A digital twin is only useful if it stays in sync with the real asset. Sensors, maintenance history and clear questions matter more than the render.",
         "/digitaltwins", "Read the digital twin guide",
         "Floating three-dimensional cubes and glowing spheres"),
    _img("passport", "photo-1581553673739-c4906b5d0de8", "Digital identity",
         "Prove who you are, not what you know",
         "Passwords prove knowledge; identity systems prove a person. The design question is how to do that without creating a single point of failure.",
         "/digitalidentity", "Read the digital identity guide",
         "Open passport with colourful ink stamps"),
    _img("rocket", "photo-1517976487492-5750f3195933", "Space tech",
         "Reusable hardware changed the maths",
         "Falling launch costs turned satellites from a national project into a commercial tool. The next fight is bandwidth, debris and orbital traffic.",
         "/spacetechnology", "Read the space technology guide",
         "Spacecraft lifting off during the day"),
    _img("code", "photo-1498050108023-c5249f4df085", "APIs",
         "Software talking to software",
         "An API is a contract: inputs, outputs and the promises in between. Good ones are boring, versioned and hard to break by accident.",
         "/apis", "Read the API guide",
         "Laptop with lines of code on the screen"),
    _img("code2", "photo-1461749280684-dccba630e2f6", "Developers",
         "Readable code is a feature",
         "Code is read far more often than it is written. Names, small functions and honest tests save more time than clever tricks.",
         "/devops", "Read the DevOps guide",
         "Monitor displaying programming code"),
    _img("laptop-glow", "photo-1785245566050-8aaa947c74b8", "DevOps",
         "Ship small, ship often",
         "Deployment pipelines turn releases from events into routine. The goal is a change you can reverse in minutes, not a perfect change.",
         "/devops", "Read the DevOps guide",
         "Glowing laptop screen on a dark reflective surface"),
    _img("laptop-desk", "photo-1643409329501-f17776d3823a", "Open source",
         "Standing on shared foundations",
         "Open source is a licence and a community, not a business model. Maintenance, security and funding are the parts that decide whether it lasts.",
         "/opensource", "Read the open source guide",
         "Laptop computer sitting on a wooden desk"),
    _img("laptop", "photo-1531297484001-80022131f5a1", "Hardware",
         "The laptop still runs the world",
         "Desktops and laptops remain where deep work happens. Battery efficiency, memory and how well the machine handles AI-assisted software decide the purchase.",
         "/techproducts", "Tech buying guides",
         "Slim laptop on a desk lit with cool blue light"),
    _img("domore", "photo-1483058712412-4245e9b90334", "Software",
         "Tools for deep work",
         "The best productivity tools disappear into a routine. Pick a small set, learn their shortcuts and stop rebuilding your system every month.",
         "/software", "Browse free tools",
         "Mac computer on a desk with the words Do More on screen"),
    _img("laptop-book", "photo-1501504905252-473c47e087f8", "Reading",
         "Context beats the headline",
         "A headline tells you something happened. A good explainer tells you why it matters and what to do next.",
         "/blog", "Read the latest analysis",
         "Laptop beside an open book on a desk"),
    _img("books", "photo-1610116306796-6fea9f4fae38", "Guides",
         "Learn one idea properly",
         "Every guide starts with the mental model, then the limits, then what to read next. No jargon, no hype.",
         "/techtopics", "Browse 35 tech guides",
         "Pile of open paperback books"),
    _img("controller", "photo-1509198397868-475647b2a1e5", "Games",
         "Take a five-minute break",
         "Eight free browser games, no downloads and no accounts. A quick reset is part of a good working day.",
         "/games", "Open Pixel Palace",
         "White game controller held in a hand"),
    _img("newspaper", "photo-1768595408288-22f8215ba8e9", "News",
         "Headlines with the context attached",
         "Fresh tech headlines linked to the guides that explain them, so a story becomes understanding instead of anxiety.",
         "/news", "Read live tech news",
         "Person in a suit holding a newspaper over their face"),
    _img("mail", "photo-1596526131083-e8c633c948d2", "Newsletter",
         "One email a week. All the signal.",
         "The AI, market and software stories that matter, plus new tools before anyone else. Free, no spam.",
         "/subscribe", "Subscribe free",
         "Mail app icon on a phone screen"),
    _img("phone-desk", "photo-1773158742082-6f26389f7492", "Contact",
         "Talk to a human",
         "Questions about a service, advertising or a free tool? Send a message and it goes straight to the inbox.",
         "/contact", "Contact Digital Infohub",
         "Person holding a phone near a laptop and coffee"),
    _img("team", "photo-1517048676732-d65bc937f952", "About",
         "Independent, and happy to stay that way",
         "Digital Infohub is a small independent publication. No venture funding, no paywall, no hidden agenda.",
         "/about", "About Digital Infohub",
         "People working together around a table"),
    _img("imac", "photo-1626785774573-4b799315345d", "Services",
         "Design and build, without the agency fog",
         "Websites, design and promotion with clear pricing and a real person on the other end.",
         "/services", "See services and pricing",
         "Desktop computer and keyboard on a clean desk"),
    _img("analytics", "photo-1460925895917-afdab827c52f", "Advertising",
         "Reach people who make decisions",
         "Put a product in front of developers, founders and technology leaders with clear, respectful advertising.",
         "/advertise", "Advertise on Digital Infohub",
         "Laptop showing an analytics dashboard"),
    _img("question", "photo-1599508704512-2f19efd1e35f", "Quiz",
         "How well do you actually know tech?",
         "Six quick quizzes with a grade for every topic and a guide for what to learn next.",
         "/quiz", "Take the tech quiz",
         "Red neon question mark on a wall"),
    _img("planner", "photo-1506784983877-45594efa4cbe", "Calendar",
         "Plan the week in one place",
         "A calendar only helps if opening it is faster than remembering. Keep it light and private.",
         "/tool-calendar", "Open the calendar",
         "Open monthly planner with a cup of coffee"),
    _img("checklist", "photo-1768055104910-8c8d213835fb", "Tasks",
         "Write it down, then finish it",
         "A short list you trust beats a long list you ignore. Capture quickly and review once a day.",
         "/tool-task-manager", "Open the task manager",
         "Hand writing a checklist in a notebook"),
    _img("writing", "photo-1517971071642-34a2d3ecc9cd", "Notes",
         "Capture first, organise later",
         "Notes are useful when they are fast to write and easy to find. Structure can wait.",
         "/tool-quick-notes", "Open quick notes",
         "Person writing on a piece of paper with a pen"),
    _img("hourglass", "photo-1518281361980-b26bfd556770", "Focus",
         "Work in blocks, rest on purpose",
         "A timer turns an open-ended task into a finish line. The break is part of the method, not a reward.",
         "/tool-pomodoro", "Start a focus timer",
         "Clear hourglass on a table"),
    _img("calculator", "photo-1648201637025-1c77b9be3013", "Money",
         "Run the numbers before the decision",
         "Simple arithmetic prevents most bad purchases. Keep a calculator one tap away.",
         "/software/calculator", "Open the calculator",
         "Calculator and pen on a piece of paper"),
    _img("receipt", "photo-1545941962-1b6654eb8072", "Budgeting",
         "Know where the money went",
         "Tracking spending works when entry takes seconds. Categories and charts come second.",
         "/tool-expense-tracker", "Open the expense tracker",
         "Printed receipt on a white surface"),
    _img("piggy", "photo-1607863680198-23d4b2565df0", "Saving",
         "Pay yourself first",
         "Saving is a system, not a resolution. Automate a small amount and increase it when income rises.",
         "/software/savesmart", "Open SaveSmart",
         "Pink piggy bank on a wooden table"),
    _img("tape", "photo-1703756291638-b1774ae3c186", "Converters",
         "Stop doing unit maths in your head",
         "A converter removes a whole class of avoidable mistakes, especially when measurements cross borders.",
         "/tool-unit-converter", "Open the unit converter",
         "Close-up of a tape measure"),
    _img("qr", "photo-1595079676339-1534801ad6cf", "QR codes",
         "A link you can print",
         "QR codes bridge paper and phones. Keep the destination short, permanent and worth scanning.",
         "/tool-qr-generator", "Open the QR generator",
         "Phone displaying a QR code"),
    _img("retro", "photo-1550745165-9bc0b252726f", "ASCII art",
         "Pictures made of characters",
         "ASCII art is a reminder that constraints breed style. Type a photo into text and see for yourself.",
         "/software/ascii-art", "Open the ASCII converter",
         "Vintage games console and joystick"),
    _img("blueprint", "photo-1762146828422-50a8bd416d3c", "Blueprints",
         "Plan before you build",
         "A clear plan saves more time than fast typing. Sketch the structure, then write the code.",
         "/software/buildengine", "Open BuildEngine",
         "Architectural blueprints spread out on a surface"),
    _img("businesscard", "photo-1718670013921-2f144aba173a", "Business cards",
         "A first impression you can hold",
         "A clean card carries a name, what you do and one way to reach you. Everything else is decoration.",
         "/software/business-card", "Open the card maker",
         "Pair of business cards on a marble counter"),
    _img("colors", "photo-1787580113284-1ebd249eb2dc", "Colour",
         "Pick colours that work together",
         "Good palettes are about contrast and hierarchy, not the number of swatches. Check the text before you ship it.",
         "/software/color-picker", "Open the colour picker",
         "Coloured pencils arranged in a spectrum"),
    _img("designbook", "photo-1561070791-2526d30994b5", "Design",
         "Design is a decision, not a decoration",
         "The interfaces people trust are the ones that explain themselves and fail gracefully.",
         "/software/graphic-design", "Open the design studio",
         "Colour swatch book used by designers"),
    _img("typography", "photo-1611532736597-de2d4265fba3", "Typography",
         "Type carries the tone",
         "A typeface sets the mood before a single word is read. Choose two weights and stick to them.",
         "/software/font-maker", "Open the font maker",
         "Tablet showing a letter A sketch with a stylus"),
    _img("cooking", "photo-1653233797467-1a528819fd4f", "Recipes",
         "Cook once, eat twice",
         "A recipe is a reusable plan. Clear steps and a shopping list make the second time easier.",
         "/software/cookinstep", "Open CookInStep",
         "Person chopping vegetables on a cutting board"),
    _img("kayak", "photo-1480480565647-1c4385c7c0bf", "Outdoors",
         "Find water worth paddling",
         "A good trip starts with conditions, distance and a way back. Check all three before you launch.",
         "/software/kayakmeocean", "Open KayakMeOcean",
         "Woman paddling a kayak on a lake"),
    _img("scrapbook", "photo-1706931333738-87738429e35b", "Scrapbook",
         "Keep the things that matter",
         "A scrapbook is a small, private archive. A few good pieces beat a folder of screenshots.",
         "/software/scrapbook", "Open the scrapbook",
         "Collage of pressed flowers and leaves"),
    _img("map", "photo-1524661135-423995f22d0b", "Travel",
         "Plan the route, not just the destination",
         "A travel plan is a list of decisions: when, where, how long and what you will skip.",
         "/software/travel-planner", "Open the travel planner",
         "World map in blue, green and yellow"),
    _img("photoedit", "photo-1744948961024-66baaafbb5dc", "Images",
         "Convert without uploading",
         "Image conversion should not require an account or a server. Keep the file on your device.",
         "/software/webp-to-png", "Open the image converter",
         "Photo editing software open on a laptop screen"),
    _img("phone", "photo-1511707171634-5f897ff02aa9", "Phones",
         "The phone is the default computer",
         "Most people meet the internet on a phone first. Speed, clarity and thumb-sized controls are not optional.",
         "/post/newest-iphone-2026", "Read the iPhone guide",
         "Smartphone showing a colourful app interface beside a laptop"),
    _img("android", "photo-1592890288564-76628a30a657", "Android",
         "Choice is the feature",
         "Android spans £150 phones and £1,500 foldables. The right model depends on the job, not the badge.",
         "/post/newest-samsung-phone-2026", "Read the Samsung guide",
         "Person holding a black Android smartphone"),
    _img("tablet", "photo-1542751110-97427bbecf20", "Tablets",
         "A screen that fits the sofa",
         "Tablets earn their place when they do one job well: reading, sketching or watching. A keyboard does not make it a laptop.",
         "/post/newest-ipad-2026", "Read the iPad guide",
         "Person holding a turned-on iPad"),
    _img("airpods", "photo-1572569511254-d8f925fe2cbb", "Audio",
         "Small speakers, big trade-offs",
         "Earbuds balance fit, battery and noise cancellation. Try the fit before you believe the spec sheet.",
         "/post/newest-airpods-2026", "Read the AirPods guide",
         "Apple AirPods in a charging case"),
    _img("settings", "photo-1760074016722-04b95a22a310", "Phone tips",
         "Fix the phone before you replace it",
         "Most slow-phone problems are storage, background apps or a tired battery. Check those first.",
         "/post/how-to-clear-cache-on-iphone", "Read the cache guide",
         "Hand holding a smartphone with colourful app icons"),
    _img("screenrecord", "photo-1560785219-cc81ab373cd3", "Screen recording",
         "Show, don't tell",
         "A short screen recording explains a bug or a workflow faster than a paragraph. Record, trim, share.",
         "/post/how-to-screen-record-on-iphone", "Read the screen recording guide",
         "Person recording someone playing guitar on a camera"),
    _img("faceid", "photo-1638951003100-2cc4550a9737", "Face ID",
         "When the sensor says no",
         "Face ID failures are usually dirt, a bad angle or a reset. Work through the simple causes before assuming hardware.",
         "/post/why-is-my-face-id-not-working", "Read the Face ID guide",
         "Person holding an iPhone in their hand"),
    _img("social", "photo-1724862936518-ae7fcfc052c1", "Social media",
         "Post less, mean more",
         "An AI assistant can draft and schedule, but taste and trust still come from a person.",
         "/post/could-babav-be-your-next-ai-social-media-assistant", "Read the Babav review",
         "Person holding a smartphone showing social media"),
    _img("study", "photo-1434030216411-0b793f4b4173", "Learning",
         "Study smarter, not longer",
         "Spaced repetition and practice questions beat re-reading. The hard part is starting small enough to keep going.",
         "/post/beating-syllabus-overload-with-smarter-medical-learning", "Read the study guide",
         "Person writing at a wooden table beside a mug"),
    _img("storefront", "photo-1575663620136-5ebbfcc2c597", "Small business",
         "Local knowledge is a real advantage",
         "A small business wins on trust, speed and knowing the customer. Local networks make that easier.",
         "/post/small-biz-philly-a-great-resource-for-local-entrepreneurs", "Read the Small Biz Philly story",
         "Open sign outside a small shop"),
    _img("future", "photo-1772550018808-ebbcc271726c", "Future tech",
         "The future arrives in pieces",
         "Most predictions fail on timing, not direction. Watch what ships, what it costs and who adopts it first.",
         "/post/what-will-tech-look-like-in-the-future", "Read the future tech analysis",
         "Silhouettes watching a bright blue swirling vortex"),
    _img("dots", "photo-1758073519996-6d3c63b4922c", "Tech intelligence",
         "One hub, everything explained",
         "Guides, tools, market context and an AI guide in one calm place. Start anywhere, go as deep as you like.",
         "/techtopics", "Browse the guides",
         "Abstract blue field of glowing technology dots"),
    _img("network", "photo-1644088379091-d574269d422f", "Networks",
         "Everything is connected now",
         "The interesting failures happen between systems. Understanding the links matters more than memorising the parts.",
         "/5gnetworks", "Explore networks",
         "Glowing blue network lines and nodes forming a mesh"),
    _img("abstract", "photo-1620641788421-7a1c342ea42e", "Digital culture",
         "Where code meets culture",
         "Product decisions are cultural decisions. The interfaces people trust tend to explain themselves.",
         "/blog", "Read the latest analysis",
         "Colourful abstract three-dimensional shapes"),
    _img("blue-abstract", "photo-1727434032773-af3cd98375ba", "Data",
         "Models are maps, not territory",
         "A model is a simplification. The useful question is always: useful for what, and wrong in which direction?",
         "/artificialintelligence", "Read the AI guide",
         "Deep blue abstract digital waves and particles"),
]

BY_ID = {image["id"]: image for image in IMAGES}


def share_url(image_id: str) -> str:
    # Force JPEG so every social crawler gets a predictable 1200x630 card.
    return _photo_url(BY_ID[image_id]["photo"], SHARE_W, SHARE_H, 80) + "&fm=jpg"


def card_url(image_id: str) -> str:
    return _photo_url(BY_ID[image_id]["photo"], CARD_W, CARD_H, 70)


def ambient_url(image_id: str) -> str:
    return _photo_url(BY_ID[image_id]["photo"], AMBIENT_W, AMBIENT_H, 40)


def image_alt(image_id: str) -> str:
    return BY_ID[image_id]["alt"]


# Social card for the main hand-authored pages.
PAGE_IMAGES = {
    "index.html": "dots",
    "blog.html": "laptop-book",
    "techtopics.html": "books",
    "software.html": "domore",
    "techproducts.html": "laptop",
    "games.html": "controller",
    "subscribe.html": "mail",
    "about.html": "team",
    "services.html": "imac",
    "advertise.html": "analytics",
    "news.html": "newspaper",
    "quiz.html": "question",
    "coincompass.html": "chart",
    "privacy-policy.html": "padlock",
    "expense-tracker.html": "receipt",
    "pomodoro.html": "hourglass",
    "contact.html": "phone-desk",
}

TOOL_IMAGES = {
    "tool-calendar.html": "planner",
    "tool-expense-tracker.html": "receipt",
    "tool-json-formatter.html": "code2",
    "tool-markdown-editor.html": "writing",
    "tool-password-generator.html": "lock-keyboard",
    "tool-pomodoro.html": "hourglass",
    "tool-qr-generator.html": "qr",
    "tool-quick-notes.html": "writing",
    "tool-task-manager.html": "checklist",
    "tool-unit-converter.html": "tape",
}

SOFTWARE_IMAGES = {
    "software/infohubgpt.html": "ai-chip",
    "software/marketlens.html": "chart",
    "software/calculator.html": "calculator",
    "software/converter.html": "tape",
    "software/cookinstep.html": "cooking",
    "software/json.html": "code2",
    "software/kayakmeocean.html": "kayak",
    "software/markdown.html": "writing",
    "software/password.html": "lock-keyboard",
    "software/savesmart.html": "piggy",
    "software/taskygpt.html": "checklist",
    "software/buildengine.html": "blueprint",
    "software/ascii-art.html": "retro",
    "software/business-card.html": "businesscard",
    "software/calendar.html": "planner",
    "software/color-picker.html": "colors",
    "software/font-maker.html": "typography",
    "software/graphic-design.html": "designbook",
    "software/html-coder.html": "code2",
    "software/marketing-assistant.html": "team",
    "software/qr-code-generator.html": "qr",
    "software/save-money-assistant.html": "piggy",
    "software/scrapbook.html": "scrapbook",
    "software/task-timer.html": "hourglass",
    "software/todo.html": "checklist",
    "software/travel-planner.html": "map",
    "software/webp-to-png.html": "photoedit",
}

TOPIC_IMAGES = {
    "artificialintelligence": "ai-chip",
    "machinelearning": "brain",
    "blockchain": "cubes",
    "cloudcomputing": "cloud-room",
    "cybersecurity": "security",
    "internetofthings": "iot",
    "quantumcomputing": "quantum",
    "bigdata": "dashboard",
    "virtualreality": "vr",
    "5gnetworks": "tower",
    "apis": "code",
    "devops": "laptop-glow",
    "opensource": "laptop-desk",
    "robotics": "robot-arm",
    "edgecomputing": "fiber",
    "web3": "bitcoin",
    "semiconductors": "circuit",
    "3dprinting": "printer",
    "biotechnology": "cells",
    "greentechnology": "wind",
    "digitaltwins": "model3d",
    "zerotrustsecurity": "security",
    "serverlesscomputing": "serverless",
    "neuromorphiccomputing": "brain",
    "augmentedreality": "vr",
    "drones": "drone",
    "nanotechnology": "microscope",
    "spacetechnology": "rocket",
    "wearabletechnology": "watch",
    "smartcities": "city",
    "spatialcomputing": "vr",
    "autonomousvehicles": "tesla",
    "digitalidentity": "passport",
    "humanoidrobots": "humanoid",
    "datacenters": "server",
}

POST_IMAGES = {
    "how-to-clear-cache-on-iphone": "settings",
    "how-to-screen-record-on-iphone": "screenrecord",
    "why-is-my-face-id-not-working": "faceid",
    "why-is-my-phone-not-charging": "phone",
    "how-to-stay-safe-online-2026": "padlock",
    "meet-miyabi-from-nomad-sculpt-to-blender": "model3d",
    "meet-teamtbm": "controller",
    "newest-airpods-2026": "airpods",
    "newest-apple-watch-2026": "fruit-watch",
    "newest-ipad-2026": "tablet",
    "newest-iphone-2026": "phone",
    "newest-samsung-phone-2026": "android",
    "quantum-computing-breakthroughs-2026": "quantum",
    "small-biz-philly-a-great-resource-for-local-entrepreneurs": "storefront",
    "tech-market-sell-off-october-2026": "chart",
    "tech-trends-october-2026": "network",
    "top-tech-headlines-sept-2026": "newspaper",
    "ai-agent-economy-october-catalysts": "ai-chip",
    "ai-hardware-race-sept-2026": "microchip",
    "ai-math-robotics-security-sept-2026": "robot-arm",
    "ai-model-wars-august-2026": "brain",
    "ai-wearables-2026": "watch",
    "beating-syllabus-overload-with-smarter-medical-learning": "study",
    "could-babav-be-your-next-ai-social-media-assistant": "social",
    "cybersecurity-ai-investment-2026": "security",
    "greygrid-studio-shows-that-great-design-doesn-t-need-to-be-loud": "designbook",
    "investment-ideas-2026": "chart",
    "what-will-tech-look-like-in-the-future": "future",
    "what-does-tech-look-like-today": "circuit",
}


def image_key_for(rel_path: str) -> str:
    """Resolve a curated image id for a page path such as 'blog.html'."""
    path = rel_path.replace("\\", "/").lstrip("./")
    name = path.rsplit("/", 1)[-1]
    if path in PAGE_IMAGES:
        return PAGE_IMAGES[path]
    if name in PAGE_IMAGES:
        return PAGE_IMAGES[name]
    if path in SOFTWARE_IMAGES:
        return SOFTWARE_IMAGES[path]
    if name in TOOL_IMAGES:
        return TOOL_IMAGES[name]
    stem = name[:-5] if name.endswith(".html") else name
    if path.startswith("post/") and stem in POST_IMAGES:
        return POST_IMAGES[stem]
    if stem in TOPIC_IMAGES:
        return TOPIC_IMAGES[stem]
    if stem in POST_IMAGES:
        return POST_IMAGES[stem]
    return "network"


def _gallery_count(kind: str) -> int:
    return {
        "home": 8,
        "blog": 6,
        "techtopics": 6,
        "post": 3,
        "tool": 3,
        "software-detail": 3,
    }.get(kind, 4)


def gallery_html(page_key: str, kind: str = "blog") -> str:
    """Clickable image cards with fresh tech context, rotated per page."""
    count = min(_gallery_count(kind), len(IMAGES))
    offset = sum(ord(ch) for ch in page_key) % len(IMAGES)
    picked = []
    seen_hrefs = set()
    for i in range(len(IMAGES)):
        img = IMAGES[(offset + i) % len(IMAGES)]
        if img["href"] in seen_hrefs:
            continue
        seen_hrefs.add(img["href"])
        picked.append(img)
        if len(picked) == count:
            break
    cards = []
    for img in picked:
        cards.append(
            f'      <a class="dih-gallery-card" href="{escape(img["href"])}">\n'
            f'        <span class="dih-gallery-media">\n'
            f'          <img src="{escape(card_url(img["id"]))}" alt="{escape(img["alt"])}" '
            f'width="{CARD_W}" height="{CARD_H}" loading="lazy" decoding="async">\n'
            f'          <span class="dih-gallery-tag">{escape(img["tag"])}</span>\n'
            f'        </span>\n'
            f'        <span class="dih-gallery-body">\n'
            f'          <strong>{escape(img["title"])}</strong>\n'
            f'          <span>{escape(img["blurb"])}</span>\n'
            f'          <em>{escape(img["cta"])} &rarr;</em>\n'
            f'        </span>\n'
            f'      </a>'
        )
    return f"""<!-- DIH:GALLERY -->
<section class="dih-gallery" aria-labelledby="dihGalleryTitle">
  <div class="dih-gallery-head">
    <div>
      <span class="dih-gallery-eyebrow">Visual briefing</span>
      <h2 id="dihGalleryTitle">Technology, in focus</h2>
      <p>Fast context on the ideas shaping the industry, with a guide for every one.</p>
    </div>
    <a class="dih-gallery-all" href="/techtopics">All 35 tech guides <span aria-hidden="true">&rarr;</span></a>
  </div>
  <div class="dih-gallery-grid">
{chr(10).join(cards)}
  </div>
  <p class="dih-gallery-credit">Photography by Unsplash contributors. Cards link to related Digital Infohub guides.</p>
</section>
<!-- /DIH:GALLERY -->"""


def ambient_html(page_key: str) -> str:
    image_id = image_key_for(page_key)
    url = escape(ambient_url(image_id))
    return (
        '<!-- DIH:AMBIENT -->\n'
        f'<div class="dih-ambient" aria-hidden="true" style="--dih-ambient:url(\'{url}\')"></div>\n'
        '<!-- /DIH:AMBIENT -->'
    )
