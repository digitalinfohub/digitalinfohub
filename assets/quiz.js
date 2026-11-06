/* Digital Infohub — six short technology quizzes with a persistent report card. */
(function () {
  'use strict';

  var QUIZZES = [
    {
      id: 'ai',
      title: 'Artificial Intelligence',
      icon: '🧠',
      desc: 'Models, training and where humans still matter.',
      guide: '/artificialintelligence',
      questions: [
        {
          q: 'What does training an AI model actually do?',
          options: ['Writes the final answers into a database', 'Adjusts the model’s parameters using examples', 'Installs the model on a user’s phone', 'Compresses the model into a smaller file'],
          answer: 1,
          why: 'Training is the optimisation step that tunes the model’s parameters so its outputs match useful examples.'
        },
        {
          q: 'Which of these is an example of narrow AI?',
          options: ['A system that can do any intellectual task', 'A spam filter that classifies email', 'A general-purpose robot butler', 'A conscious machine'],
          answer: 1,
          why: 'A spam filter is built for one well-defined task. Almost every deployed AI system today is narrow.'
        },
        {
          q: 'What is inference?',
          options: ['Running a trained model on new input', 'Collecting the training data', 'Cleaning and labelling a dataset', 'Designing the model architecture'],
          answer: 0,
          why: 'Inference is the cheap, high-volume step where a trained model produces an answer for new input.'
        },
        {
          q: 'Why can a large language model invent facts?',
          options: ['It searches every website in real time', 'It predicts likely text rather than verified truth', 'It only uses peer-reviewed sources', 'It refuses to answer uncertain questions'],
          answer: 1,
          why: 'Language models generate statistically likely text. A fluent answer can still be false, so important claims need verification.'
        },
        {
          q: 'What is the safest approach for a high-stakes AI decision?',
          options: ['Publish the output without review', 'Trust the model if the answer is well written', 'Keep a human review and check the evidence', 'Use the largest model available'],
          answer: 2,
          why: 'High-stakes decisions need human accountability, source checks and a clear path to challenge the output.'
        }
      ]
    },
    {
      id: 'security',
      title: 'Cybersecurity',
      icon: '🛡️',
      desc: 'Identity, phishing and the controls that reduce real risk.',
      guide: '/cybersecurity',
      questions: [
        {
          q: 'Which control most directly protects an account when a password is stolen?',
          options: ['A longer password reset link', 'Multi-factor authentication or passkeys', 'A custom browser theme', 'A second email address'],
          answer: 1,
          why: 'MFA and passkeys add a factor an attacker does not have, so a stolen password alone is not enough.'
        },
        {
          q: 'What is phishing?',
          options: ['A technique for speeding up a network', 'A fraudulent message designed to steal credentials or install malware', 'A way to encrypt a hard drive', 'A backup strategy'],
          answer: 1,
          why: 'Phishing tricks a person into revealing information or running something malicious, often by impersonating a trusted service.'
        },
        {
          q: 'What does “zero trust” mean in practice?',
          options: ['Trust every device inside the office network', 'Verify every request instead of trusting the network perimeter', 'Remove all firewalls', 'Give every employee admin access'],
          answer: 1,
          why: 'Zero trust treats identity and context as the basis for access, rather than assuming a network location is safe.'
        },
        {
          q: 'What does ransomware usually do?',
          options: ['Encrypts data and demands payment', 'Only slows down a website', 'Deletes the operating system immediately', 'Steals a monitor’s display settings'],
          answer: 0,
          why: 'Ransomware typically encrypts or exfiltrates data and demands payment for restoration or non-disclosure.'
        },
        {
          q: 'What makes a backup genuinely useful in a ransomware incident?',
          options: ['It is stored on the same drive as the original', 'It is offline or immutable and has been tested', 'It is never checked after creation', 'It is emailed to the same account'],
          answer: 1,
          why: 'An isolated, tested backup is not reachable by the attacker and can actually be restored when needed.'
        }
      ]
    },
    {
      id: 'cloud',
      title: 'Cloud Computing',
      icon: '☁️',
      desc: 'Rented infrastructure, shared responsibility and the cost drivers.',
      guide: '/cloudcomputing',
      questions: [
        {
          q: 'What does IaaS provide?',
          options: ['A finished SaaS application', 'Virtual machines, storage and networking', 'Only a managed database', 'A design system for mobile apps'],
          answer: 1,
          why: 'Infrastructure as a service rents the base compute, storage and network layer; you manage the operating system and application.'
        },
        {
          q: 'What is object storage designed for?',
          options: ['Storing files as objects in buckets', 'Running relational SQL queries', 'Rendering graphics on a GPU', 'Replacing a content delivery network'],
          answer: 0,
          why: 'Object storage keeps data as objects with metadata in buckets, which is ideal for files, media and backups.'
        },
        {
          q: 'What does auto-scaling do?',
          options: ['Adds or removes capacity as demand changes', 'Encrypts every database row', 'Moves all workloads to one server', 'Deletes idle user accounts'],
          answer: 0,
          why: 'Auto-scaling adjusts capacity to match traffic, reducing overload during peaks and waste during quiet periods.'
        },
        {
          q: 'Why does cloud region choice affect latency?',
          options: ['Regions change the programming language', 'Physical distance adds network round-trip time', 'Every region has a different internet speed limit', 'Regions only affect billing currency'],
          answer: 1,
          why: 'Data has to travel. Placing a service near its users reduces the round-trip time and improves responsiveness.'
        },
        {
          q: 'Under the shared responsibility model, what does the customer always own?',
          options: ['The physical data centre security', 'The provider’s hypervisor patches', 'Their data, identities and configuration', 'The global network backbone'],
          answer: 2,
          why: 'The provider secures the cloud infrastructure; the customer remains responsible for data, access and how services are configured.'
        }
      ]
    },
    {
      id: 'blockchain',
      title: 'Blockchain',
      icon: '⛓️',
      desc: 'Shared ledgers, smart contracts and when not to use a chain.',
      guide: '/blockchain',
      questions: [
        {
          q: 'What is a blockchain?',
          options: ['A shared, append-only record maintained by multiple parties', 'A faster kind of relational database', 'A programming language for mobile apps', 'A type of cloud storage bucket'],
          answer: 0,
          why: 'A blockchain is a replicated ledger whose history is hard to rewrite quietly, which is useful when no single party should control the record.'
        },
        {
          q: 'What is a smart contract?',
          options: ['A legal document stored as a PDF', 'Code that executes on a blockchain', 'A customer support chatbot', 'A hardware wallet'],
          answer: 1,
          why: 'A smart contract is program code deployed to a chain. It runs deterministically when its conditions are met.'
        },
        {
          q: 'What is consensus in a blockchain network?',
          options: ['A vote on the price of a token', 'The process by which nodes agree on valid state', 'A way to compress blocks', 'A customer identity check'],
          answer: 1,
          why: 'Consensus rules let independent nodes agree on which transactions and blocks are valid without a central referee.'
        },
        {
          q: 'Which key actually controls funds in a self-custody wallet?',
          options: ['The public address', 'The private key or seed phrase', 'The block explorer URL', 'The token’s ticker symbol'],
          answer: 1,
          why: 'The private key authorises transactions. Anyone who has it can move the funds, which is why it must never be shared.'
        },
        {
          q: 'When is a traditional database usually the better choice?',
          options: ['When several untrusted parties need a shared record', 'When one trusted operator needs fast, flexible queries', 'When you want irreversible public settlement', 'When you need a token'],
          answer: 1,
          why: 'A normal database is simpler, faster and cheaper when a trusted operator can manage the data. A chain adds cost and complexity that may not be justified.'
        }
      ]
    },
    {
      id: 'quantum',
      title: 'Quantum Computing',
      icon: '⚛️',
      desc: 'Qubits, error correction and the encryption migration.',
      guide: '/quantumcomputing',
      questions: [
        {
          q: 'What is a qubit?',
          options: ['A classical bit that is always 0 or 1', 'A quantum unit of information that can exist in superposition', 'A type of GPU core', 'A encryption key'],
          answer: 1,
          why: 'A qubit can occupy a superposition of states and can be entangled with other qubits, enabling different kinds of computation.'
        },
        {
          q: 'Which problem is quantum computing expected to accelerate?',
          options: ['Sending email', 'Factoring large numbers and simulating quantum systems', 'Rendering a static web page', 'Storing files in a bucket'],
          answer: 1,
          why: 'Shor’s algorithm threatens widely used public-key cryptography, and quantum simulation is a natural fit for quantum hardware.'
        },
        {
          q: 'Why is error correction such a big deal for quantum computers?',
          options: ['Qubits are too fast', 'Qubits are fragile and accumulate errors from noise', 'Error correction makes screens brighter', 'It reduces the need for cooling'],
          answer: 1,
          why: 'Quantum states decohere easily. Useful machines need many physical qubits working together as one logical, error-corrected qubit.'
        },
        {
          q: 'What is post-quantum cryptography?',
          options: ['Encryption that only runs on quantum computers', 'New classical algorithms designed to resist quantum attacks', 'A way to cool a data centre', 'A blockchain consensus method'],
          answer: 1,
          why: 'Post-quantum algorithms run on ordinary computers but are designed to remain secure against known quantum attacks.'
        },
        {
          q: 'Where is quantum computing today?',
          options: ['Every phone has a useful quantum chip', 'It is in an early, noisy era with limited practical applications', 'It has fully replaced classical computers', 'It only exists in science fiction'],
          answer: 1,
          why: 'Current devices are experimental and error-prone. Some narrow demonstrations are useful, but broad practical advantage is still emerging.'
        }
      ]
    },
    {
      id: 'iot',
      title: 'Internet of Things',
      icon: '📡',
      desc: 'Sensors, gateways and the security questions every device raises.',
      guide: '/internetofthings',
      questions: [
        {
          q: 'What is the Internet of Things?',
          options: ['A social network for devices', 'A network of physical devices with sensors and connectivity', 'A cloud billing model', 'A programming language'],
          answer: 1,
          why: 'IoT describes physical objects that collect and exchange data over a network, often with little or no human involvement.'
        },
        {
          q: 'What is the job of an IoT gateway?',
          options: ['To replace every sensor', 'To aggregate and route data between devices and the cloud', 'To render a user interface', 'To generate encryption keys for the whole internet'],
          answer: 1,
          why: 'A gateway bridges local device protocols and the wider network, reducing the number of direct connections and adding local processing.'
        },
        {
          q: 'What is a common IoT security failure?',
          options: ['Using default passwords and unpatched firmware', 'Encrypting all traffic', 'Segmenting the device network', 'Disabling unused ports'],
          answer: 0,
          why: 'Default credentials and neglected firmware are recurring weaknesses because devices are numerous, long-lived and often hard to update.'
        },
        {
          q: 'Why process data at the edge instead of sending everything to the cloud?',
          options: ['To increase latency', 'To reduce latency, bandwidth use and exposure of raw data', 'To make devices heavier', 'To avoid using sensors'],
          answer: 1,
          why: 'Local processing can answer in milliseconds, avoid shipping raw video or audio, and keep sensitive data closer to its source.'
        },
        {
          q: 'Which protocol is commonly used for lightweight IoT messaging?',
          options: ['SMTP', 'MQTT', 'FTP', 'SSH'],
          answer: 1,
          why: 'MQTT is a lightweight publish/subscribe protocol designed for constrained devices and unreliable networks.'
        }
      ]
    }
  ];

  var STORE = 'dih_quiz_scores_v1';
  var current = 0;
  var scores = readScores();

  var tabs = document.getElementById('quizTabs');
  var form = document.getElementById('quizForm');
  var title = document.getElementById('quizTopicTitle');
  var desc = document.getElementById('quizTopicDesc');
  var icon = document.getElementById('quizTopicIcon');
  var progress = document.getElementById('quizProgress');
  var result = document.getElementById('quizResult');
  var report = document.getElementById('quizReport');
  var overall = document.getElementById('quizOverall');
  if (!tabs || !form) return;

  function readScores() {
    try {
      var parsed = JSON.parse(localStorage.getItem(STORE) || '{}');
      return parsed && typeof parsed === 'object' ? parsed : {};
    } catch (e) { return {}; }
  }

  function saveScores() {
    try { localStorage.setItem(STORE, JSON.stringify(scores)); } catch (e) {}
  }

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (ch) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch];
    });
  }

  function letter(pct) {
    if (pct >= 90) return 'A';
    if (pct >= 80) return 'B';
    if (pct >= 70) return 'C';
    if (pct >= 60) return 'D';
    return 'F';
  }

  function bestFor(id) {
    var entry = scores[id];
    return entry && typeof entry.pct === 'number' ? entry : null;
  }

  function renderTabs() {
    tabs.innerHTML = QUIZZES.map(function (quiz, index) {
      var best = bestFor(quiz.id);
      return '<button type="button" class="dih-quiz-tab' + (index === current ? ' is-active' : '') + '" role="tab" aria-selected="' + (index === current ? 'true' : 'false') + '" data-quiz-tab="' + index + '">' +
        '<span aria-hidden="true">' + quiz.icon + '</span><span>' + esc(quiz.title) + '</span>' +
        (best ? '<em class="dih-quiz-tab-grade grade-' + letter(best.pct).toLowerCase() + '">' + letter(best.pct) + '</em>' : '') +
        '</button>';
    }).join('');
    tabs.querySelectorAll('[data-quiz-tab]').forEach(function (button) {
      button.addEventListener('click', function () { selectQuiz(Number(button.getAttribute('data-quiz-tab'))); });
    });
  }

  function renderQuestion(quiz, question, index) {
    return '<fieldset class="dih-quiz-q">' +
      '<legend><span class="dih-q-num">' + (index + 1) + '</span>' + esc(question.q) + '</legend>' +
      '<div class="dih-quiz-options">' +
      question.options.map(function (option, optionIndex) {
        var id = quiz.id + '-q' + index + '-o' + optionIndex;
        return '<label class="dih-quiz-option" for="' + id + '">' +
          '<input id="' + id + '" type="radio" name="q' + index + '" value="' + optionIndex + '">' +
          '<span class="dih-quiz-radio" aria-hidden="true"></span>' +
          '<span>' + esc(option) + '</span>' +
        '</label>';
      }).join('') +
      '</div>' +
    '</fieldset>';
  }

  function selectQuiz(index) {
    current = Math.max(0, Math.min(QUIZZES.length - 1, index));
    var quiz = QUIZZES[current];
    icon.textContent = quiz.icon;
    title.textContent = quiz.title;
    desc.textContent = quiz.desc;
    form.innerHTML = quiz.questions.map(function (question, i) { return renderQuestion(quiz, question, i); }).join('');
    result.innerHTML = '';
    result.className = 'dih-quiz-result';
    updateProgress();
    renderTabs();
    if (history.replaceState) history.replaceState(null, '', '#' + quiz.id);
  }

  function updateProgress() {
    var checked = form.querySelectorAll('input[type="radio"]:checked').length;
    progress.textContent = checked + ' / ' + QUIZZES[current].questions.length;
  }

  function renderReport() {
    var attempted = QUIZZES.filter(function (quiz) { return !!bestFor(quiz.id); });
    report.innerHTML = QUIZZES.map(function (quiz) {
      var best = bestFor(quiz.id);
      if (!best) {
        return '<div class="dih-report-row is-empty"><span>' + quiz.icon + '</span><div><strong>' + esc(quiz.title) + '</strong><small>Not attempted yet</small></div><em>—</em></div>';
      }
      var grade = letter(best.pct);
      return '<div class="dih-report-row"><span>' + quiz.icon + '</span><div><strong>' + esc(quiz.title) + '</strong><small>' + best.correct + ' / ' + best.total + ' correct</small></div><em class="dih-report-grade grade-' + grade.toLowerCase() + '">' + grade + '</em></div>';
    }).join('');

    if (!attempted.length) {
      overall.innerHTML = '<strong>No scores yet.</strong><span>Pick a topic and answer five questions to start your report card.</span>';
      return;
    }
    var total = attempted.reduce(function (sum, quiz) { return sum + bestFor(quiz.id).pct; }, 0);
    var average = Math.round(total / attempted.length);
    overall.innerHTML = '<div class="dih-overall-score"><b>' + average + '%</b><span>average across ' + attempted.length + ' topic' + (attempted.length === 1 ? '' : 's') + '</span></div>' +
      '<div class="dih-overall-bar"><span style="width:' + average + '%"></span></div>' +
      '<p>Overall grade <strong>' + letter(average) + '</strong>. ' + (average >= 80 ? 'Strong foundation — try a topic you have not attempted.' : 'Pick the lowest score and read the linked guide, then retake it.') + '</p>';
  }

  function gradeQuiz(event) {
    event.preventDefault();
    var quiz = QUIZZES[current];
    var answers = quiz.questions.map(function (_, index) {
      var selected = form.querySelector('input[name="q' + index + '"]:checked');
      return selected ? Number(selected.value) : -1;
    });
    if (answers.some(function (answer) { return answer < 0; })) {
      result.className = 'dih-quiz-result is-warning';
      result.innerHTML = '<strong>Answer all five questions first.</strong><span>You can change any answer before grading.</span>';
      return;
    }

    var correct = answers.reduce(function (sum, answer, index) { return sum + (answer === quiz.questions[index].answer ? 1 : 0); }, 0);
    var pct = Math.round((correct / quiz.questions.length) * 100);
    var grade = letter(pct);
    var previous = bestFor(quiz.id);
    if (!previous || pct > previous.pct) {
      scores[quiz.id] = { correct: correct, total: quiz.questions.length, pct: pct, at: new Date().toISOString() };
      saveScores();
    }

    quiz.questions.forEach(function (question, index) {
      var fieldset = form.querySelectorAll('.dih-quiz-q')[index];
      var selected = form.querySelector('input[name="q' + index + '"]:checked');
      fieldset.classList.add('is-graded');
      fieldset.querySelectorAll('.dih-quiz-option').forEach(function (label, optionIndex) {
        label.classList.toggle('is-correct', optionIndex === question.answer);
        label.classList.toggle('is-wrong', !!selected && Number(selected.value) === optionIndex && optionIndex !== question.answer);
      });
      var explanation = document.createElement('p');
      explanation.className = 'dih-quiz-why';
      explanation.innerHTML = '<strong>' + (answers[index] === question.answer ? 'Correct.' : 'Not quite.') + '</strong> ' + esc(question.why);
      fieldset.appendChild(explanation);
    });

    result.className = 'dih-quiz-result is-graded grade-' + grade.toLowerCase();
    result.innerHTML = '<div class="dih-result-score"><b>' + pct + '%</b><span>' + correct + ' of ' + quiz.questions.length + ' correct</span></div>' +
      '<div class="dih-result-copy"><strong>Grade ' + grade + '</strong><p>' + (pct >= 80 ? 'Strong work. You have the mental model — try a topic you have not attempted yet.' : pct >= 60 ? 'Solid start. Read the linked guide and retake this topic to lock it in.' : 'Worth another pass. The guide below covers the gaps without the jargon.') + '</p>' +
      '<div class="dih-result-links"><a href="' + quiz.guide + '">Read the ' + esc(quiz.title) + ' guide →</a>' +
      (current < QUIZZES.length - 1 ? '<button type="button" id="quizNext">Next topic: ' + esc(QUIZZES[current + 1].title) + ' →</button>' : '<button type="button" id="quizNext">Back to the first topic →</button>') +
      '</div></div>';
    var next = document.getElementById('quizNext');
    if (next) next.addEventListener('click', function () { selectQuiz(current < QUIZZES.length - 1 ? current + 1 : 0); });
    renderTabs();
    renderReport();
  }

  form.addEventListener('change', updateProgress);
  form.addEventListener('submit', gradeQuiz);

  document.getElementById('quizReset').addEventListener('click', function () {
    form.reset();
    form.querySelectorAll('.dih-quiz-q').forEach(function (fieldset) { fieldset.classList.remove('is-graded'); });
    form.querySelectorAll('.dih-quiz-why').forEach(function (note) { note.remove(); });
    result.innerHTML = '';
    result.className = 'dih-quiz-result';
    updateProgress();
  });

  document.getElementById('quizClearAll').addEventListener('click', function () {
    if (!window.confirm('Clear every saved quiz score in this browser?')) return;
    scores = {};
    saveScores();
    renderTabs();
    renderReport();
    result.innerHTML = '';
    result.className = 'dih-quiz-result';
  });

  var hash = (location.hash || '').replace('#', '');
  var initial = QUIZZES.findIndex(function (quiz) { return quiz.id === hash; });
  selectQuiz(initial >= 0 ? initial : 0);
  renderReport();
})();
