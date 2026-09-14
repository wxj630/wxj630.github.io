(function () {
  "use strict";

  function slugify(text, usedIds) {
    var base = text
      .toLowerCase()
      .replace(/\s+/g, "-")
      .replace(/[^\w\u3400-\u9fff-]/g, "")
      .replace(/^-+|-+$/g, "");

    if (!base) {
      base = "section";
    }

    var id = base;
    var suffix = 2;
    while (usedIds[id] || document.getElementById(id)) {
      id = base + "-" + suffix;
      suffix += 1;
    }
    usedIds[id] = true;
    return id;
  }

  function setActiveLink(links, activeId) {
    links.forEach(function (link) {
      var isActive = link.getAttribute("href") === "#" + activeId;
      link.classList.toggle("is-active", isActive);
      if (isActive) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  function initializeTableOfContents() {
    var body = document.querySelector(".blog-post-body");
    var toc = document.getElementById("blog-toc");
    var list = document.getElementById("blog-toc-list");

    if (!body || !toc || !list) {
      return;
    }

    var headings = Array.prototype.slice.call(body.querySelectorAll("h2, h3, h4"));
    if (!headings.length) {
      return;
    }

    var usedIds = {};
    Array.prototype.forEach.call(body.querySelectorAll("[id]"), function (node) {
      usedIds[node.id] = true;
    });

    var stack = [{ level: 1, list: list, lastItem: null }];

    headings.forEach(function (heading) {
      var level = parseInt(heading.tagName.substring(1), 10);
      if (!heading.id) {
        heading.id = slugify(heading.textContent.trim(), usedIds);
      } else {
        usedIds[heading.id] = true;
      }

      while (stack.length > 1 && level <= stack[stack.length - 1].level) {
        stack.pop();
      }

      var current = stack[stack.length - 1];
      var targetList = current.list;

      if (level > current.level && current.lastItem) {
        targetList = current.lastItem.querySelector(":scope > ol");
        if (!targetList) {
          targetList = document.createElement("ol");
          current.lastItem.appendChild(targetList);
        }
      }

      var item = document.createElement("li");
      var link = document.createElement("a");
      link.href = "#" + heading.id;
      link.textContent = heading.textContent.trim();
      item.appendChild(link);
      targetList.appendChild(item);
      stack.push({ level: level, list: targetList, lastItem: item });
    });

    toc.hidden = false;

    var links = Array.prototype.slice.call(list.querySelectorAll("a"));
    function updateActiveLink() {
      var activeHeading = headings[0];
      var activationOffset = 150;

      headings.forEach(function (heading) {
        if (heading.getBoundingClientRect().top <= activationOffset) {
          activeHeading = heading;
        }
      });

      setActiveLink(links, activeHeading.id);
    }

    updateActiveLink();
    window.addEventListener("scroll", updateActiveLink, { passive: true });
    window.addEventListener("resize", updateActiveLink);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeTableOfContents);
  } else {
    initializeTableOfContents();
  }
})();
