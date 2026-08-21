/* ============================================
   APLIK DECOR — SCRIPT GLOBAL & CONVERSÃO
   ============================================ */

// ⚠️ LINK CENTRAL DO FORMULÁRIO DO CONTRATANTE
// Todos os botões de ação e CTAs levam a este link para garantir a conversão e qualificação completa do Lead!
const CTA_URL = "https://SEU-FORMULARIO-AQUI.com";

// URLs de navegação interna
const LP = {
  home:     "./index.html",
  piso:     "./piso-vinilico.html",
  boiserie: "./boiserie.html",
  papel:    "./papel-de-parede.html"
};

/* ── Todos os CTAs vão 100% para o Formulário ─ */
function applyCTA() {
  document.querySelectorAll("[data-cta='form'], [data-cta='whatsapp'], .float-cta, .mobile-sticky-bar a").forEach(el => {
    el.href = CTA_URL;
    el.target = "_blank";
    el.rel = "noopener noreferrer";
  });
  
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

/* ── Before & After Interactive Slider ─── */
function initBeforeAfter() {
  const sliders = document.querySelectorAll(".ba-container");
  sliders.forEach(slider => {
    const after = slider.querySelector(".ba-after");
    const handle = slider.querySelector(".ba-handle");
    if (!after || !handle) return;

    let isDragging = false;

    const setPosition = (clientX) => {
      const rect = slider.getBoundingClientRect();
      let pos = ((clientX - rect.left) / rect.width) * 100;
      if (pos < 0) pos = 0;
      if (pos > 100) pos = 100;
      after.style.width = pos + "%";
      handle.style.left = pos + "%";
    };

    slider.addEventListener("mousedown", (e) => {
      isDragging = true;
      setPosition(e.clientX);
    });

    window.addEventListener("mouseup", () => { isDragging = false; });
    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      setPosition(e.clientX);
    });

    slider.addEventListener("touchstart", (e) => {
      isDragging = true;
      if (e.touches[0]) setPosition(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener("touchend", () => { isDragging = false; });
    window.addEventListener("touchmove", (e) => {
      if (!isDragging) return;
      if (e.touches[0]) setPosition(e.touches[0].clientX);
    }, { passive: true });
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
          <a href="#" class="btn btn-gold btn-sm" data-cta="form">Solicitar Orçamento Deste Modelo</a>
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
  initBeforeAfter();
  initLightbox();
  initWallpaperFilter();
  initAnimations();
});
