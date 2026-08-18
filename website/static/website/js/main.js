const header = document.getElementById("site-header");
const toggle = document.getElementById("nav-toggle");
const overlay = document.getElementById("nav-overlay");

document.body.classList.add("js-ready");

const onScroll = () => {
    header?.classList.toggle("is-scrolled", window.scrollY > 20);
};
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

const setMenu = (open) => {
    if (!toggle || !overlay) return;
    toggle.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.body.classList.toggle("menu-open", open);
    if (open) {
        overlay.removeAttribute("hidden");
    } else {
        overlay.setAttribute("hidden", "");
    }
};

toggle?.addEventListener("click", () => {
    setMenu(overlay?.hasAttribute("hidden"));
});

overlay?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setMenu(false));
});

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setMenu(false);
});

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-in");
                observer.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.16, rootMargin: "0px 0px -8% 0px" }
);

document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const heroVideo = document.querySelector("[data-home-hero-video]");
if (heroVideo) {
    const revealAndPlay = () => {
        heroVideo.classList.add("is-visible");
        if (prefersReducedMotion) return;
        const playAttempt = heroVideo.play();
        if (playAttempt && typeof playAttempt.catch === "function") {
            playAttempt.catch(() => {});
        }
    };

    heroVideo.addEventListener("canplay", revealAndPlay, { once: true });

    if (heroVideo.readyState >= 3) {
        revealAndPlay();
    } else {
        heroVideo.load();
    }
}

const waitForImages = (root) =>
    Promise.all(
        [...root.querySelectorAll("img")].map((img) =>
            img.complete
                ? Promise.resolve()
                : new Promise((resolve) => {
                      img.addEventListener("load", resolve, { once: true });
                      img.addEventListener("error", resolve, { once: true });
                  })
        )
    );

document.querySelectorAll("[data-marquee]").forEach((root) => {
    const track = root.querySelector("[data-marquee-track]");
    if (!track || prefersReducedMotion) return;

    const source = track.querySelector(".home-marquee-set") || track;
    const originals = [...source.children].map((node) => node.cloneNode(true));
    if (!originals.length) return;

    const speed = Number(root.dataset.marqueeSpeed) || 24;

    const hideClone = (node) => {
        node.setAttribute("aria-hidden", "true");
        node.setAttribute("tabindex", "-1");
        node.querySelectorAll("a, button").forEach((el) => el.setAttribute("tabindex", "-1"));
    };

    const makeSet = (hidden) => {
        const set = document.createElement("div");
        set.className = "home-marquee-set";
        originals.forEach((node) => set.appendChild(node.cloneNode(true)));
        if (hidden) hideClone(set);
        return set;
    };

    const setup = () => {
        track.style.animation = "none";
        track.style.transform = "none";
        track.replaceChildren();

        const firstSet = makeSet(false);
        track.appendChild(firstSet);
        const setWidth = firstSet.offsetWidth;
        if (!setWidth) return;

        let total = setWidth;
        let copies = 1;
        while (total < root.offsetWidth + setWidth && copies < 12) {
            track.appendChild(makeSet(true));
            total += setWidth;
            copies += 1;
        }

        track.style.setProperty("--marquee-distance", `-${setWidth}px`);
        track.style.setProperty("--marquee-duration", `${Math.max(setWidth / speed, 40)}s`);
        track.getBoundingClientRect();
        track.style.animation = "";
        track.style.transform = "";
        root.classList.add("is-ready");
    };

    waitForImages(track).then(setup);

    let resizeTimer;
    window.addEventListener("resize", () => {
        window.clearTimeout(resizeTimer);
        resizeTimer = window.setTimeout(setup, 150);
    });
});

const carousel = document.querySelector("[data-carousel]");
if (carousel) {
    const slides = [...carousel.querySelectorAll(".hero-slide")];
    const dots = [...document.querySelectorAll("[data-carousel-dots] button")];
    const prev = document.querySelector("[data-carousel-prev]");
    const next = document.querySelector("[data-carousel-next]");
    let index = 0;
    let timer;

    const show = (nextIndex) => {
        if (!slides.length) return;
        slides[index]?.classList.remove("is-active");
        dots[index]?.classList.remove("is-active");
        index = (nextIndex + slides.length) % slides.length;
        slides[index].classList.add("is-active");
        dots[index]?.classList.add("is-active");
    };

    const start = () => {
        stop();
        if (slides.length < 2) return;
        timer = window.setInterval(() => show(index + 1), 6500);
    };

    const stop = () => {
        if (timer) window.clearInterval(timer);
    };

    prev?.addEventListener("click", () => {
        show(index - 1);
        start();
    });
    next?.addEventListener("click", () => {
        show(index + 1);
        start();
    });
    dots.forEach((dot, i) => {
        dot.addEventListener("click", () => {
            show(i);
            start();
        });
    });

    carousel.addEventListener("mouseenter", stop);
    carousel.addEventListener("mouseleave", start);
    start();
}

document.querySelectorAll(".focus-accordion details").forEach((detail) => {
    detail.addEventListener("toggle", () => {
        if (!detail.open) return;
        const group = detail.closest(".focus-accordion");
        group?.querySelectorAll("details").forEach((other) => {
            if (other !== detail) {
                other.open = false;
            }
        });
    });
});

document.querySelectorAll("[data-tabbed-section]").forEach((root) => {
    const tabs = [...root.querySelectorAll("[data-tab]")];
    const panels = [...root.querySelectorAll("[data-panel]")];

    const replayPanelAnimations = (panel) => {
        panel.querySelectorAll(".partner-checklist li, .partner-tags li, .accountability-card").forEach((item) => {
            item.style.animation = "none";
            item.getBoundingClientRect();
            item.style.animation = "";
        });
    };

    const showPanel = (name) => {
        tabs.forEach((tab) => {
            const isActive = tab.dataset.tab === name;
            tab.classList.toggle("is-active", isActive);
            tab.setAttribute("aria-selected", String(isActive));
        });

        panels.forEach((panel) => {
            const isActive = panel.dataset.panel === name;
            panel.classList.toggle("is-active", isActive);
            panel.hidden = !isActive;
            if (isActive) {
                replayPanelAnimations(panel);
            }
        });
    };

    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            showPanel(tab.dataset.tab);
        });
    });
});

const animateCount = (element) => {
    const target = Number(element.dataset.count);
    if (Number.isNaN(target)) return;
    const suffix = element.dataset.suffix || "";
    const prefix = element.dataset.prefix || "";
    const duration = 1200;
    const start = performance.now();

    const step = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - (1 - progress) ** 3;
        element.textContent = `${prefix}${Math.round(target * eased)}${suffix}`;
        if (progress < 1) {
            requestAnimationFrame(step);
        }
    };

    requestAnimationFrame(step);
};

const countObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.querySelectorAll("[data-count]").forEach((counter) => {
                if (counter.dataset.counted) return;
                counter.dataset.counted = "true";
                animateCount(counter);
            });
            countObserver.unobserve(entry.target);
        });
    },
    { threshold: 0.35 }
);

document.querySelectorAll(".impact-stat-card, .impact-metric, .home-stat-card").forEach((item) => {
    countObserver.observe(item);
});

document.querySelectorAll("[data-portfolio-filters]").forEach((root) => {
    const grid = root.querySelector("[data-portfolio-grid]");
    const cards = [...root.querySelectorAll("[data-portfolio-grid] .portfolio-card")];
    const sourceCards = cards.map((card) => card.cloneNode(true));
    const emptyState = root.querySelector("[data-portfolio-empty]");
    const clearButton = root.querySelector("[data-portfolio-clear]");
    const count = root.querySelector("[data-portfolio-count]");
    const dropdowns = [...root.querySelectorAll("[data-filter-dropdown]")];
    const filters = { status: "", deal_type: "" };

    const closeAllDropdowns = (except) => {
        dropdowns.forEach((dropdown) => {
            if (dropdown === except) return;
            dropdown.classList.remove("is-open");
            dropdown.querySelector(".filter-dropdown-trigger")?.setAttribute("aria-expanded", "false");
            dropdown.querySelector(".filter-dropdown-menu")?.setAttribute("hidden", "");
        });
    };

    const setDropdownValue = (dropdown, value) => {
        const options = [...dropdown.querySelectorAll("[role='option']")];
        const selected = options.find((option) => option.dataset.value === value) || options[0];
        options.forEach((option) => {
            option.classList.toggle("is-selected", option === selected);
            option.setAttribute("aria-selected", option === selected ? "true" : "false");
        });
        dropdown.querySelector(".filter-dropdown-value").textContent = selected.textContent;
    };

    const matchesFilters = (card, nextFilters) => {
        const matchesStatus = !nextFilters.status || card.dataset.status === nextFilters.status;
        const matchesDealType = !nextFilters.deal_type || card.dataset.dealType === nextFilters.deal_type;
        return matchesStatus && matchesDealType;
    };

    const updateOptionAvailability = () => {
        dropdowns.forEach((dropdown) => {
            const key = dropdown.dataset.filterKey;
            const otherFilters = { ...filters, [key]: "" };
            dropdown.querySelectorAll("[role='option']").forEach((option) => {
                if (!option.dataset.value) {
                    option.disabled = false;
                    option.hidden = false;
                    return;
                }

                const previewFilters = { ...otherFilters, [key]: option.dataset.value };
                const hasMatches = sourceCards.some((card) => matchesFilters(card, previewFilters));
                option.disabled = !hasMatches;
                option.hidden = !hasMatches;
            });
        });
    };

    const applyFilters = () => {
        const visibleCards = sourceCards.filter((card) => matchesFilters(card, filters));
        if (grid) {
            grid.replaceChildren(...visibleCards.map((card) => card.cloneNode(true)));
        }

        emptyState.hidden = visibleCards.length > 0;
        clearButton.hidden = !filters.status && !filters.deal_type;
        if (count) {
            count.textContent = `Showing ${visibleCards.length} investment${visibleCards.length === 1 ? "" : "s"}`;
        }
        updateOptionAvailability();

        const params = new URLSearchParams();
        if (filters.status) params.set("status", filters.status);
        if (filters.deal_type) params.set("deal_type", filters.deal_type);
        const query = params.toString();
        const nextUrl = query ? `${window.location.pathname}?${query}` : window.location.pathname;
        window.history.replaceState({}, "", nextUrl);
    };

    dropdowns.forEach((dropdown) => {
        const key = dropdown.dataset.filterKey;
        const trigger = dropdown.querySelector(".filter-dropdown-trigger");
        const menu = dropdown.querySelector(".filter-dropdown-menu");

        trigger?.addEventListener("click", () => {
            const willOpen = !dropdown.classList.contains("is-open");
            closeAllDropdowns(dropdown);
            dropdown.classList.toggle("is-open", willOpen);
            trigger.setAttribute("aria-expanded", String(willOpen));
            menu.toggleAttribute("hidden", !willOpen);
        });

        dropdown.querySelectorAll("[role='option']").forEach((option) => {
            option.addEventListener("click", () => {
                if (option.disabled) return;
                filters[key] = option.dataset.value || "";
                setDropdownValue(dropdown, filters[key]);
                dropdown.classList.remove("is-open");
                trigger.setAttribute("aria-expanded", "false");
                menu.setAttribute("hidden", "");
                applyFilters();
            });
        });
    });

    clearButton?.addEventListener("click", () => {
        filters.status = "";
        filters.deal_type = "";
        dropdowns.forEach((dropdown) => setDropdownValue(dropdown, ""));
        applyFilters();
    });

    document.addEventListener("click", (event) => {
        if (event.target.closest("[data-filter-dropdown]")) return;
        closeAllDropdowns();
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") closeAllDropdowns();
    });

    const params = new URLSearchParams(window.location.search);
    filters.status = params.get("status") || "";
    filters.deal_type = params.get("deal_type") || "";

    dropdowns.forEach((dropdown) => {
        const key = dropdown.dataset.filterKey;
        setDropdownValue(dropdown, filters[key] || "");
    });

    applyFilters();
});
