import streamlit as st


def render_section(title: str, items: list[dict]) -> None:
    st.markdown(f"### {title}")
    for ref in items:
        parts: list[str] = []
        if ref.get("authors"):
            parts.append(ref["authors"])  # already formatted "Last, F.; Last, F."
        if ref.get("year"):
            parts.append(str(ref["year"]))
        header = ", ".join(parts) if parts else ""

        journal_parts: list[str] = []
        if ref.get("journal"):
            journal_parts.append(ref["journal"])  # Journal or Book/Publisher
        if ref.get("volume"):
            journal_parts.append(f"{ref['volume']}")
        if ref.get("issue"):
            journal_parts.append(f"({ref['issue']})")
        if ref.get("pages"):
            journal_parts.append(f"{ref['pages']}")
        journal_str = ", ".join(journal_parts)

        link_str = ""
        if ref.get("doi"):
            link_str = f" DOI: [{ref['doi']}]({ref.get('url') or ''})"
        elif ref.get("url"):
            link_str = f" URL: [{ref['url']}]({ref['url']})"

        st.markdown(
            f"- <em>{ref['title']}</em>{f' — {header}' if header else ''}{f'. {journal_str}.' if journal_str else ''}{link_str}",
            unsafe_allow_html=True,
        )


def main() -> None:
    st.markdown("## References")
    st.markdown("These references are selected from a larger collection assembled for a related project. Some references may be more directly relevant in future updates to this project.")

    # Core LV and stability
    render_section(
        "Core Lotka–Volterra and Stability",
        [
            {
                "title": "Predator–Prey Models: A Review of Some Recent Advances",
                "authors": "Diz-Pita, É.; Otero-Espinar, M. V.",
                "year": 2021,
                "journal": "Mathematics",
                "volume": "9",
                "issue": "15",
                "pages": "1783",
                "doi": "10.3390/math9151783",
                "url": "https://www.mdpi.com/2227-7390/9/15/1783",
            },
            {
                "title": "Graphical Representation and Stability Conditions of Predator-Prey Interactions",
                "authors": "Rosenzweig, M. L.; MacArthur, R. H.",
                "year": 1963,
                "journal": "The American Naturalist",
                "volume": "97",
                "issue": "895",
                "pages": "209–223",
                "doi": "10.1086/282272",
                "url": "https://www.journals.uchicago.edu/doi/10.1086/282272",
            },
            {
                "title": "Limit Cycles in Predator-Prey Communities",
                "authors": "May, R. M.",
                "year": 1972,
                "journal": "Science",
                "volume": "177",
                "issue": "4052",
                "pages": "900–902",
                "doi": "10.1126/science.177.4052.900",
                "url": "https://www.science.org/doi/10.1126/science.177.4052.900",
            },
            {
                "title": "Simple mathematical models with very complicated dynamics",
                "authors": "May, R. M.",
                "year": 1976,
                "journal": "",
                "volume": "",
                "issue": "",
                "pages": "",
                "doi": "",
                "url": "",
            },
        ],
    )

    # Predation and functional responses
    render_section(
        "Predation and Functional Responses",
        [
            {
                "title": "Some Characteristics of Simple Types of Predation and Parasitism",
                "authors": "Holling, C. S.",
                "year": 1959,
                "journal": "The Canadian Entomologist",
                "volume": "91",
                "issue": "7",
                "pages": "385–398",
                "doi": "10.4039/Ent91385-7",
                "url": "https://www.cambridge.org/core/product/identifier/S0008347X00072692/type/journal_article",
            },
            {
                "title": "The Functional Response of Predators to Prey Density and its Role in Mimicry and Population Regulation",
                "authors": "Holling, C. S.",
                "year": 1965,
                "journal": "Memoirs of the Entomological Society of Canada",
                "volume": "97",
                "issue": "S45",
                "pages": "5–60",
                "doi": "10.4039/entm9745fv",
                "url": "https://www.cambridge.org/core/product/identifier/S0071075X00000862/type/journal_article",
            },
            {
                "title": "Coupling in predator-prey dynamics: Ratio-Dependence",
                "authors": "Arditi, R.; Ginzburg, L. R.",
                "year": 1989,
                "journal": "Journal of Theoretical Biology",
                "volume": "139",
                "issue": "3",
                "pages": "311–326",
                "doi": "10.1016/S0022-5193(89)80211-5",
                "url": "https://linkinghub.elsevier.com/retrieve/pii/S0022519389802115",
            },
            {
                "title": "The nature of predation: prey dependent, ratio dependent or neither?",
                "authors": "Abrams, P. A.; Ginzburg, L. R.",
                "year": 2000,
                "journal": "Trends in Ecology & Evolution",
                "volume": "15",
                "issue": "8",
                "pages": "337–341",
                "doi": "10.1016/S0169-5347(00)01908-X",
                "url": "https://linkinghub.elsevier.com/retrieve/pii/S016953470001908X",
            },
        ],
    )

    # Adaptive / behavioral predation
    render_section(
        "Adaptive and Behavioral Predation",
        [
            {
                "title": "Putting predators back into behavioral predator–prey interactions",
                "authors": "Lima, S. L.",
                "year": 2002,
                "journal": "Trends in Ecology & Evolution",
                "volume": "17",
                "issue": "2",
                "pages": "70–75",
                "doi": "10.1016/S0169-5347(01)02393-X",
                "url": "https://linkinghub.elsevier.com/retrieve/pii/S016953470102393X",
            }
        ],
    )

    # Individual-based modeling and complexity
    render_section(
        "Individual-Based Modeling and Complexity",
        [
            {
                "title": "Individual-based models in ecology after four decades",
                "authors": "DeAngelis, D. L.; Grimm, V.",
                "year": 2014,
                "journal": "F1000Prime Reports",
                "volume": "6",
                "issue": "",
                "pages": "39",
                "doi": "10.12703/P6-39",
                "url": "https://facultyopinions.com/prime/reports/b/6/39/",
            },
            {
                "title": "FROM INDIVIDUALS TO POPULATION DENSITIES: SEARCHING FOR THE INTERMEDIATE SCALE OF NONTRIVIAL DETERMINISM",
                "authors": "Pascual, M.; Levin, S. A.",
                "year": 1999,
                "journal": "",
                "volume": "",
                "issue": "",
                "pages": "",
                "doi": "",
                "url": "",
            },
        ],
    )

    # Wolves: empirical and applied studies
    render_section(
        "Empirical Studies: Wolves and Ungulates",
        [
            {
                "title": "Modelling territoriality and wolf–deer interactions",
                "authors": "Lewis, M. A.; Murray, J. D.",
                "year": 1993,
                "journal": "Nature",
                "volume": "366",
                "issue": "6457",
                "pages": "738–740",
                "doi": "10.1038/366738a0",
                "url": "https://www.nature.com/articles/366738a0",
            },
            {
                "title": "Predicting prey population dynamics from kill rate, predation rate and predator-prey ratios in three wolf-ungulate systems",
                "authors": "Vucetich, J. A.; Hebblewhite, M.; Smith, D. W.; Peterson, R. O.",
                "year": 2011,
                "journal": "Journal of Animal Ecology",
                "volume": "80",
                "issue": "6",
                "pages": "1236–1245",
                "doi": "10.1111/j.1365-2656.2011.01855.x",
                "url": "https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2656.2011.01855.x",
            },
            {
                "title": "Seasonal patterns of predation for gray wolves in the multi‐prey system of Yellowstone National Park",
                "authors": "Metz, M. C.; Smith, D. W.; Vucetich, J. A.; Stahler, D. R.; Peterson, R. O.",
                "year": 2012,
                "journal": "Journal of Animal Ecology",
                "volume": "81",
                "issue": "3",
                "pages": "553–563",
                "doi": "10.1111/j.1365-2656.2011.01945.x",
                "url": "https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2656.2011.01945.x",
            },
            {
                "title": "The adaptive value of morphological, behavioural and life‐history traits in reproductive female wolves",
                "authors": "Stahler, D. R.; MacNulty, D. R.; Wayne, R. K.; vonHoldt, B.; Smith, D. W.; Pelletier, F.",
                "year": 2013,
                "journal": "Journal of Animal Ecology",
                "volume": "82",
                "issue": "1",
                "pages": "222–234",
                "doi": "10.1111/j.1365-2656.2012.02039.x",
                "url": "https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2656.2012.02039.x",
            },
            {
                "title": "Predator‐dependent functional response in wolves: from food limitation to surplus killing",
                "authors": "Zimmermann, B.; Sand, H.; Wabakken, P.; Liberg, O.; Andreassen, H. P.; Coulson, T.",
                "year": 2015,
                "journal": "Journal of Animal Ecology",
                "volume": "84",
                "issue": "1",
                "pages": "102–112",
                "doi": "10.1111/1365-2656.12280",
                "url": "https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2656.12280",
            },
        ],
    )

    # Resilience framing
    render_section(
        "Resilience",
        [
            {
                "title": "Resilience and Stability of Ecological Systems",
                "authors": "Holling, C. S.",
                "year": "",
                "journal": "",
                "volume": "",
                "issue": "",
                "pages": "",
                "doi": "",
                "url": "",
            },
            {
                "title": "Resilience, Adaptability and Transformability in Social-ecological Systems",
                "authors": "Walker, B.; Holling, C. S.; Carpenter, S. R.; Kinzig, A. P.",
                "year": 2004,
                "journal": "Ecology and Society",
                "volume": "9",
                "issue": "2",
                "pages": "art5",
                "doi": "10.5751/ES-00650-090205",
                "url": "http://www.ecologyandsociety.org/vol9/iss2/art5/",
            },
        ],
    )

    # Math background
    render_section(
        "Mathematical Background",
        [
            {
                "title": "Differential equations, dynamical systems, and linear algebra",
                "authors": "Hirsch, M. W.; Smale, S.",
                "year": 1974,
                "journal": "Academic Press (Book)",
                "volume": "",
                "issue": "",
                "pages": "",
                "doi": "",
                "url": "",
            }
        ],
    )

    st.divider()
    st.markdown("### Quick Navigation")
    st.page_link("pages/home.py", label="Home", icon="🏠")


main()


