/* ============================================
   APLIK DECOR — SCRIPT GLOBAL & CONVERSÃO
   ============================================ */

// ⚠️ LINKS OFICIAIS DOS FORMULÁRIOS RESPONDI APP
const FORMS = {
  papel:    "https://form.respondi.app/eNDWZlpi", // Papel de Parede
  piso:     "https://form.respondi.app/vMvwoiIA", // Piso Vinílico
  boiserie: "https://form.respondi.app/ZEn7u8cu"  // Moldura Boiserie
};

// URLs de navegação interna
const LP = {
  home:     "./index.html",
  piso:     "./piso-vinilico.html",
  boiserie: "./boiserie.html",
  papel:    "./papel-de-parede.html"
};

/* ── Atribuição inteligente dos links de conversão ── */
function applyCTA() {
  const currentPath = window.location.pathname.toLowerCase();
  
  // Determina o formulário da página atual
  let defaultForm = FORMS.piso;
  if (currentPath.includes("papel")) {
    defaultForm = FORMS.papel;
  } else if (currentPath.includes("boiserie")) {
    defaultForm = FORMS.boiserie;
  } else if (currentPath.includes("piso")) {
    defaultForm = FORMS.piso;
  }

  // Aplica aos botões gerais de conversão
  document.querySelectorAll("[data-cta='form'], [data-cta='whatsapp'], .float-cta, .mobile-sticky-bar a").forEach(el => {
    // Se for na Home e o botão não tiver produto específico, leva para a escolha ou form
    if (currentPath.endsWith("index.html") || currentPath.endsWith("/")) {
      if (el.id === "hero-cta-main" || el.id === "header-cta" || el.id === "final-cta" || el.classList.contains("float-cta")) {
        el.href = FORMS.piso; // Form padrão institucional
      } else {
        el.href = defaultForm;
      }
    } else {
      el.href = defaultForm;
    }
    el.target = "_blank";
    el.rel = "noopener noreferrer";
  });
  
  // CTAs com direcionamento explícito por produto
  document.querySelectorAll("[data-cta='form-piso']").forEach(el => { el.href = FORMS.piso; el.target = "_blank"; el.rel = "noopener noreferrer"; });
  document.querySelectorAll("[data-cta='form-boiserie']").forEach(el => { el.href = FORMS.boiserie; el.target = "_blank"; el.rel = "noopener noreferrer"; });
  document.querySelectorAll("[data-cta='form-papel']").forEach(el => { el.href = FORMS.papel; el.target = "_blank"; el.rel = "noopener noreferrer"; });

  // Links internos de navegação entre LPs
  document.querySelectorAll("[data-cta='piso']").forEach(el => { el.href = LP.piso; });
  document.querySelectorAll("[data-cta='boiserie']").forEach(el => { el.href = LP.boiserie; });
  document.querySelectorAll("[data-cta='papel']").forEach(el => { el.href = LP.papel; });
}

/* ── Header scroll & Sticky Mobile Bar ──── */
function initHeaderAndStickyBar() {
  const h = document.querySelector(".header");
  const stickyBar = document.querySelector(".mobile-sticky-bar");

  const onScroll = () => {
    const y = window.scrollY;
    if (h) h.classList.toggle("scrolled", y > 30);
    if (stickyBar) stickyBar.classList.toggle("visible", y > 240);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
}

/* ── Mobile menu ───────────────────────── */
function initMenu() {
  const btn  = document.getElementById("menu-toggle");
  const menu = document.getElementById("mobile-menu");
  if (!btn || !menu) return;

  btn.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    btn.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open);
    document.body.style.overflow = open ? "hidden" : "";
  });

  menu.querySelectorAll("a").forEach(a => {
    a.addEventListener("click", () => {
      menu.classList.remove("open");
      btn.classList.remove("open");
      document.body.style.overflow = "";
    });
  });
}

/* ── FAQ Accordion ─────────────────────── */
function initFAQ() {
  document.querySelectorAll(".faq-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const item = btn.closest(".faq-item");
      const body = item.querySelector(".faq-body");
      const isOpen = item.classList.contains("open");

      document.querySelectorAll(".faq-item.open").forEach(el => {
        el.classList.remove("open");
        el.querySelector(".faq-body").style.maxHeight = "0";
      });

      if (!isOpen) {
        item.classList.add("open");
        body.style.maxHeight = body.scrollHeight + "px";
      }
    });
  });
}

/* ── Lightbox Modal ─────────────────────── */
function initLightbox() {
  if (!document.getElementById("aplik-lightbox")) {
    const lb = document.createElement("div");
    lb.id = "aplik-lightbox";
    lb.className = "lightbox";
    lb.innerHTML = `
      <div class="lightbox-box">
        <button class="lightbox-close" aria-label="Fechar">&times;</button>
        <div class="lightbox-img-wrap">
          <img src="" alt="" id="lightbox-img">
        </div>
        <div class="lightbox-footer">
          <span class="lightbox-title" id="lightbox-title">Aplik Decor</span>
          <a href="#" class="btn btn-gold btn-sm" data-cta="form">Quero Encontrar Minha Solução</a>
        </div>
      </div>
    `;
    document.body.appendChild(lb);
    applyCTA();
  }

  const lightbox = document.getElementById("aplik-lightbox");
  const lbImg = document.getElementById("lightbox-img");
  const lbTitle = document.getElementById("lightbox-title");
  const lbClose = lightbox.querySelector(".lightbox-close");

  const openLightbox = (src, title) => {
    lbImg.src = src;
    lbTitle.textContent = title || "Projeto Aplik Decor";
    lightbox.classList.add("open");
    document.body.style.overflow = "hidden";
  };

  const closeLightbox = () => {
    lightbox.classList.remove("open");
    document.body.style.overflow = "";
  };

  if (lbClose) lbClose.addEventListener("click", closeLightbox);
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && lightbox.classList.contains("open")) closeLightbox();
  });

  document.querySelectorAll(".gitem, .style-item, .zoomable").forEach(item => {
    item.classList.add("zoomable");
    item.addEventListener("click", () => {
      const img = item.querySelector("img");
      const label = item.querySelector(".gitem-label, .style-lbl, .ambient-lbl");
      if (img) {
        openLightbox(img.src, label ? label.textContent : img.alt);
      }
    });
  });
}

/* ── Wallpaper Filter ──────────────────── */
function initWallpaperFilter() {
  const filterBtns = document.querySelectorAll(".filter-btn");
  const styleItems = document.querySelectorAll(".style-item");
  if (!filterBtns.length || !styleItems.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const cat = btn.getAttribute("data-filter");

      styleItems.forEach(item => {
        const itemCat = item.getAttribute("data-category") || "";
        if (cat === "all" || itemCat.includes(cat)) {
          item.classList.remove("hide");
        } else {
          item.classList.add("hide");
        }
      });
    });
  });
}

/* ── Scroll animations ─────────────────── */
function initAnimations() {
  const io = new IntersectionObserver(
    (entries) => entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add("on");
        io.unobserve(e.target);
      }
    }),
    { threshold: 0.08, rootMargin: "0px 0px -32px 0px" }
  );
  document.querySelectorAll("[data-anim]").forEach(el => io.observe(el));
}

/* ── Init ──────────────────────────────── */
document.addEventListener("DOMContentLoaded", () => {
  applyCTA();
  initHeaderAndStickyBar();
  initMenu();
  initFAQ();
  initLightbox();
  initWallpaperFilter();
  initAnimations();
});
