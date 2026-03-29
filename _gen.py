content = r'''const oceanData = {
  "Atlantski okean": {
    key: "atlantic",
    area: "106.46",
    depth: "10,994 m",
    image:
      "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?auto=format&fit=crop&w=800&q=80",
  },
  "Tihii okean": {
    key: "pacific",
    area: "165.25",
    depth: "10,994 m",
    image:
      "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
  },
  "Indijski okean": {
    key: "indian",
    area: "70.56",
    depth: "7,450 m",
    image:
      "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
  },
  "Severni Ledni okean": {
    key: "arctic",
    area: "14.06",
    depth: "5,450 m",
    image:
      "https://images.unsplash.com/photo-1476673160081-cf065607f449?auto=format&fit=crop&w=800&q=80",
  },
  "Juzni Ledni okean": {
    key: "southern",
    area: "21.96",
    depth: "7,236 m",
    image:
      "https://images.unsplash.com/photo-1468581264429-2548ef9eb732?auto=format&fit=crop&w=800&q=80",
  },
};

const oceanNames = {
  sr: {
    "Atlantski okean": "Atlantski okean",
    "Tihii okean": "Tihi okean",
    "Indijski okean": "Indijski okean",
    "Severni Ledni okean": "Severni Ledeni okean",
    "Juzni Ledni okean": "Južni Ledeni okean",
  },
  en: {
    "Atlantski okean": "Atlantic Ocean",
    "Tihii okean": "Pacific Ocean",
    "Indijski okean": "Indian Ocean",
    "Severni Ledni okean": "Arctic Ocean",
    "Juzni Ledni okean": "Southern Ocean",
  },
};

const oceanDescriptions = {
  sr: {
    atlantic:
      "Drugi po veličini okean na svetu, proteže se između Amerika na zapadu i Evrope i Afrike na istoku.",
    pacific:
      "Najveći i najdublji okean, pokriva više od trećine Zemljine površine.",
    indian:
      "Treći po veličini okean, poznat po toplim vodama i bogatom morskom životu.",
    arctic:
      "Najmanji i najplići okean, većim delom pokriven ledom tokom cele godine.",
    southern:
      "Okružuje Antarktik i predstavlja dom za jedinstvene polarne ekosisteme.",
  },
  en: {
    atlantic:
      "The second-largest ocean in the world, stretching between the Americas to the west and Europe and Africa to the east.",
    pacific:
      "The largest and deepest ocean, covering more than a third of Earth's surface.",
    indian:
      "The third-largest ocean, known for its warm waters and rich marine life.",
    arctic:
      "The smallest and shallowest ocean, mostly covered in ice throughout the year.",
    southern:
      "Surrounds Antarctica and is home to unique polar ecosystems.",
  },
};

const oceanLabels = {
  sr: { area: "Površina", depth: "Maks. dubina" },
  en: { area: "Area", depth: "Max. depth" },
};

const loginStrings = {
  sr: {
    error: "Pogrešno korisničko ime ili lozinka.",
    cryptoError:
      "Potrebno je pokrenuti sajt sa lokalnog servera (HTTPS/localhost).",
    logout: "Odjavi se",
  },
  en: {
    error: "Incorrect username or password.",
    cryptoError:
      "Please run the site from a local server (HTTPS/localhost).",
    logout: "Logout",
  },
};

const currentLang = document.documentElement.lang || "sr";
const basePath = currentLang === "en" ? "../" : "";

function setActiveNav() {
  const currentPage =
    window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".navbar-arctic .nav-link").forEach((link) => {
    link.classList.remove("active");
    const href = link.getAttribute("href");
    if (href === currentPage) {
      link.classList.add("active");
    }
  });
}

function checkLoginState() {
  const loggedInUser = sessionStorage.getItem("okeansveta_user");
  const loginItem = document.getElementById("nav-login-item");

  if (!loginItem) return;

  if (loggedInUser) {
    loginItem.innerHTML = `
      <div class="nav-user-info">
        <span class="username-display">${escapeHtml(loggedInUser)}</span>
        <button class="btn-logout" id="btn-logout">${loginStrings[currentLang].logout}</button>
      </div>
    `;
    document.getElementById("btn-logout").addEventListener("click", logout);
  }
}

function logout() {
  sessionStorage.removeItem("okeansveta_user");
  window.location.reload();
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

function initNavbarScroll() {
  const navbar = document.querySelector(".navbar-arctic");
  if (!navbar) return;

  const onScroll = () => {
    if (window.scrollY > 50) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
}

function initContactForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;

  const nameField = document.getElementById("contact-name");
  const emailField = document.getElementById("contact-email");
  const messageField = document.getElementById("contact-message");

  const regexName = /^[A-Za-zÀ-žČčĆćŠšŽžĐđ\s]{2,50}$/;
  const regexEmail = /^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$/;
  const regexMessage = /^[\s\S]{10,500}$/;

  [nameField, emailField, messageField].forEach((field) => {
    const hintEl = document.getElementById(field.id + "-hint");
    const errorEl = document.getElementById(field.id + "-error");

    field.addEventListener("focus", () => {
      if (hintEl) hintEl.classList.add("visible");
      if (errorEl) errorEl.classList.remove("visible");
    });

    field.addEventListener("blur", () => {
      if (hintEl) hintEl.classList.remove("visible");
    });
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    let valid = true;

    if (!regexName.test(nameField.value.trim())) {
      showFieldError("contact-name");
      valid = false;
    } else {
      clearFieldError("contact-name");
    }

    if (!regexEmail.test(emailField.value.trim())) {
      showFieldError("contact-email");
      valid = false;
    } else {
      clearFieldError("contact-email");
    }

    if (!regexMessage.test(messageField.value)) {
      showFieldError("contact-message");
      valid = false;
    } else {
      clearFieldError("contact-message");
    }

    if (valid) {
      const successPage = currentLang === "en" ? "success.html" : "uspeh.html";
      window.location.href = successPage;
    }
  });
}

function showFieldError(fieldId) {
  const field = document.getElementById(fieldId);
  const errorEl = document.getElementById(fieldId + "-error");
  if (field) field.classList.add("is-invalid");
  if (field) field.classList.remove("is-valid");
  if (errorEl) errorEl.classList.add("visible");
}

function clearFieldError(fieldId) {
  const field = document.getElementById(fieldId);
  const errorEl = document.getElementById(fieldId + "-error");
  if (field) field.classList.remove("is-invalid");
  if (field) field.classList.add("is-valid");
  if (errorEl) errorEl.classList.remove("visible");
}

function initLoginForm() {
  const form = document.getElementById("login-form");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("login-username").value.trim();
    const password = document.getElementById("login-password").value;
    const errorEl = document.getElementById("login-error-msg");

    if (!username || !password) {
      showLoginError(errorEl, loginStrings[currentLang].error);
      return;
    }

    if (!window.crypto || !window.crypto.subtle) {
      showLoginError(errorEl, loginStrings[currentLang].cryptoError);
      return;
    }

    try {
      const hashedPassword = await hashSHA256(password);

      const response = await fetch(basePath + "users.json");
      const users = await response.json();

      const user = users.find(
        (u) => u.username === username && u.password === hashedPassword,
      );

      if (user) {
        sessionStorage.setItem("okeansveta_user", user.username);
        window.location.href = "index.html";
      } else {
        showLoginError(errorEl, loginStrings[currentLang].error);
      }
    } catch (err) {
      showLoginError(errorEl, loginStrings[currentLang].error);
    }
  });
}

function showLoginError(el, msg) {
  if (!el) return;
  el.textContent = msg;
  el.classList.add("visible");
}

async function hashSHA256(str) {
  const encoder = new TextEncoder();
  const data = encoder.encode(str);
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
}

function initOceansPage() {
  const grid = document.getElementById("ocean-grid");
  if (!grid) return;

  const loaderEl = document.getElementById("ocean-loader");
  const errorEl = document.getElementById("ocean-error");

  fetchOceanData(grid, loaderEl, errorEl);
}

async function fetchOceanData(grid, loaderEl, errorEl) {
  if (loaderEl) loaderEl.style.display = "block";
  if (errorEl) errorEl.style.display = "none";
  grid.innerHTML = "";

  try {
    const response = await fetch(
      "https://vebdizajn-4.onrender.com/api/vebdizajn/okeani",
    );
    if (!response.ok) throw new Error("API error");
    const data = await response.json();

    window._oceanApiData = data;

    if (loaderEl) loaderEl.style.display = "none";
    renderOceanCards(data);
  } catch (err) {
    if (loaderEl) loaderEl.style.display = "none";
    if (errorEl) errorEl.style.display = "block";

    const retryBtn = errorEl ? errorEl.querySelector(".btn-retry") : null;
    if (retryBtn) {
      retryBtn.onclick = () => fetchOceanData(grid, loaderEl, errorEl);
    }
  }
}

function renderOceanCards(data) {
  const grid = document.getElementById("ocean-grid");
  if (!grid) return;

  const descriptions = oceanDescriptions[currentLang];
  const labels = oceanLabels[currentLang];
  const names = oceanNames[currentLang];

  grid.innerHTML = "";

  for (const [apiName, animalsStr] of Object.entries(data)) {
    const enrichment = oceanData[apiName] || {};
    const displayName = names[apiName] || apiName;
    const description = descriptions[enrichment.key] || "";
    const animals = animalsStr.split(",").map((a) => a.trim());
    const imageUrl = enrichment.image || "";

    const card = document.createElement("div");
    card.className = "col-lg-4 col-md-6 mb-4";

    card.innerHTML = `
      <div class="card-arctic">
        <div class="card-img-wrapper">
          <img src="${imageUrl}" alt="${escapeHtml(displayName)}" loading="lazy">
        </div>
        <div class="card-body">
          <h3 class="card-title">${escapeHtml(displayName)}</h3>
          <p class="card-text">${escapeHtml(description)}</p>
          <div class="animal-tags">
            ${animals.map((a) => `<span class="animal-tag">${escapeHtml(a)}</span>`).join("")}
          </div>
          <div class="card-meta">
            <span>📐 ${labels.area}: ${enrichment.area || "—"} M km²</span>
            <span>🌊 ${labels.depth}: ${enrichment.depth || "—"}</span>
          </div>
        </div>
      </div>
    `;

    grid.appendChild(card);
  }
}

function initGallery() {
  const galleryItems = document.querySelectorAll(".gallery-item");
  if (!galleryItems.length) return;

  galleryItems.forEach((item) => {
    item.addEventListener("click", () => {
      const imgSrc =
        item.querySelector("img").getAttribute("data-full") ||
        item.querySelector("img").src;
      const captionEl = item.querySelector(".gallery-caption");
      const caption = captionEl ? captionEl.textContent : "";

      const modalImg = document.getElementById("lightbox-img");
      const modalCaption = document.getElementById("lightbox-caption");

      if (modalImg) modalImg.src = imgSrc;
      if (modalCaption) modalCaption.textContent = caption;

      const modal = new bootstrap.Modal(
        document.getElementById("galleryLightbox"),
      );
      modal.show();
    });
  });
}

function initSuccessCountdown() {
  const countdownEl = document.getElementById("countdown-number");
  if (!countdownEl) return;

  let seconds = 5;
  countdownEl.textContent = seconds;

  const interval = setInterval(() => {
    seconds--;
    countdownEl.textContent = seconds;

    if (seconds <= 0) {
      clearInterval(interval);
      window.location.href = "index.html";
    }
  }, 1000);
}

document.addEventListener("DOMContentLoaded", () => {
  setActiveNav();
  checkLoginState();
  initNavbarScroll();

  initContactForm();
  initLoginForm();
  initOceansPage();
  initGallery();
  initSuccessCountdown();
});
'''

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done - wrote', len(content), 'chars')
