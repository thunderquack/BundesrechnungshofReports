from brh_reports.crawler import _parse_search_page


def test_parse_search_page_extracts_candidates_and_next_url() -> None:
    html = """
    <p id="resultCount">1 - 2 von 132 Ergebnissen</p>
    <section aria-labelledby="resultCount" class="searchresult">
      <div class="teaser type-1 Report row">
        <div class="small-12 columns">
          <h3 class="withHeader">
            Bericht Eins
            <span class="aural">Schwerpunktthema:</span>
            <span class="category">
              <span class="aural">Dokumenttyp:</span>
              Bericht
              <span class="aural">Datum:</span>
              13.04.2026
            </span>
          </h3>
          <p>Beratungsbericht an das Ministerium</p>
          <p><a href="/SharedDocs/Downloads/DE/Berichte/2026/bericht-eins.pdf?__blob=publicationFile&v=1" class="c-button">Volltext</a></p>
        </div>
      </div>
      <div class="teaser type-1 Report row">
        <div class="small-12 columns">
          <h3 class="withHeader">
            Bericht Zwei
            <span class="aural">Schwerpunktthema:</span>
            <span class="category">
              <span class="aural">Dokumenttyp:</span>
              Bericht
              <span class="aural">Datum:</span>
              07.04.2026
            </span>
          </h3>
          <p>Abschließende Mitteilung</p>
          <p><a href="/SharedDocs/Downloads/DE/Berichte/2026/bericht-zwei.pdf?__blob=publicationFile&v=2" class="c-button">Volltext</a></p>
        </div>
      </div>
    </section>
    <nav class="navIndex">
      <ul>
        <li><a href="SiteGlobals/Forms/Suche/Berichtssuche/Berichtssuche_Formular.html?pageNo=0&amp;gtp=20916_list%253D2&amp;resultsPerPage=50" class="forward button">Weiter</a></li>
      </ul>
    </nav>
    """

    candidates, next_url, total_results = _parse_search_page(
        html,
        current_url="https://www.bundesrechnungshof.de/start",
        base_url="https://www.bundesrechnungshof.de/",
    )

    assert total_results == 132
    assert next_url == "2"
    assert len(candidates) == 2
    assert candidates[0].title == "Bericht Eins"
    assert candidates[0].published_on == "13.04.2026"
    assert candidates[0].summary == "Beratungsbericht an das Ministerium"
    assert candidates[0].pdf_url == (
        "https://www.bundesrechnungshof.de/"
        "SharedDocs/Downloads/DE/Berichte/2026/bericht-eins.pdf?__blob=publicationFile&v=1"
    )
