Bericht nach § 88 Absatz 2 BHO
an die Bundesregierung

# **Chief Data Scientists und Datenlabore** **in der Bundesverwaltung**


Teil 2 – Infrastruktur, Informationssicherheit und Wirtschaftlichkeit


13. April 2026


**Geschäftszeichen: VII 3 - 0002615/2**


Dieser Bericht enthält das vom Bundesrechnungshof abschließend im Sinne des § 96 Absatz 4 BHO festgestellte
[Prüfungsergebnis. Er ist auf www.bundesrechnungshof.de veröffentlicht.](http://www.bundesrechnungshof.de/)


Dieser Bericht des Bundesrechnungshofes ist urheberrechtlich geschützt.


## **Inhaltsverzeichnis**

**0** **Zusammenfassung.................................................................................................................. 7**


**1** **Vorbemerkung ........................................................................................................................ 13**


1.1 Datenanalyse, künstliche Intelligenz und Datenmanagement ........................................... 13


1.2 Datenstrategie der Bundesregierung ..................................................................................... 13


1.3 Chief Data Scientists und Datenlabore ................................................................................... 14


1.4 Datenpolitische Gremienstruktur ............................................................................................ 16


1.5 Querschnittliche Erhebung des Bundesrechnungshofes .................................................... 17


**2** **Infrastruktur und IT-Dienstleister ................................................................................. 17**


2.1 Infrastruktur ................................................................................................................................ 17


2.2 IT-Dienstleister ............................................................................................................................ 22


**3** **Wirtschaftlichkeit ................................................................................................................. 25**


3.1 Sachverhalt .................................................................................................................................. 25


3.2 Würdigung ................................................................................................................................... 27


3.3 Empfehlung ................................................................................................................................. 28


3.4 Stellungnahme............................................................................................................................ 29


3.5 Abschließende Würdigung ....................................................................................................... 29


**4** **Datenschutz ............................................................................................................................ 30**


4.1 Sachverhalt .................................................................................................................................. 30


4.2 Würdigung ................................................................................................................................... 31


4.3 Empfehlung ................................................................................................................................. 31


4.4 Stellungnahme............................................................................................................................ 31


4.5 Abschließende Würdigung ....................................................................................................... 32


**5** **Informationssicherheit und Geheimschutz .............................................................. 32**


5.1 Sachverhalt .................................................................................................................................. 32


5.2 Würdigung ................................................................................................................................... 34


5.3 Empfehlung ................................................................................................................................. 34


5.4 Stellungnahme............................................................................................................................ 35


5.5 Abschließende Würdigung ....................................................................................................... 35


#### **3**


**6** **IT-Betrieb ................................................................................................................................. 35**


6.1 Sachverhalt .................................................................................................................................. 35


6.2 Würdigung ................................................................................................................................... 37


6.3 Empfehlung ................................................................................................................................. 38


6.4 Stellungnahme............................................................................................................................ 38


6.5 Abschließende Würdigung ....................................................................................................... 38


**7** **Fazit ............................................................................................................................................ 39**


7.1 Stellungnahme............................................................................................................................ 40


7.2 Abschließende Würdigung ....................................................................................................... 40


#### **4**


## **Abkürzungsverzeichnis**

##### **A**

AA _Auswärtiges Amt_

##### **B**


BeschA _Beschaffungsamt des_ _Bundesministeriums des Innern_


BMDS _Bundesministerium für Digitales und Staatsmodernisierung_


BMI _Bundesministerium des Innern_


BPA _Presse- und_ _Informationsamt der Bundesregierung_


BSI _Bundesamt für Sicherheit in der_ _Informationstechnik_

##### **C**


CDO _Chief Data Officer_


CDS _Chief Data Scientist_

##### **D**


DA _Datenanalyse_


Digitalpolitische St-Runde _Digitalpolitische Runde der Staatssekretärinnen und -sekretäre der_


_Ressorts_


DM _Datenmanagement_


DSFA _Datenschutz-Folgenabschätzung_


DSGVO _Datenschutz-Grundverordnung_

##### **I**


IMAG Datenlabore _Interministerielle Arbeitsgruppe der Datenlabore_


ISK _Informationssicherheitskonzept_


ITZBund _Informationstechnikzentrum Bund_

##### **K**


KI _Künstliche Intelligenz_

##### **L**


LLM _Große Sprachmodelle_

##### **O**


ODK _Open-Data-Koordinatorin oder -Koordinator_


#### **5**


##### **P**

pbD _Personenbezogene Daten_


PLAIN _Platform Analysis and Information System_

##### **U**


UP Bund _Umsetzungsplan Bund 2017_

##### **V**


VS _Verschlusssache_


VSA _Verschlusssachenanweisung_


VS-NfD _Verschlusssache – NUR FÜR DEN DIENSTGEBRAUCH_

##### **W**


WiBe _Wirtschaftlichkeitsbetrachtung_


#### **6**


## **0 Zusammenfassung**

_Der Bundesrechnungshof hat die Chief Data Scientists (CDS), Chief Data Officers (CDO) und_


_Datenlabore im Bundeskanzleramt, den Bundesministerien (ohne Bundesministerium für_


_Digitales und Staatsmodernisierung, BMDS) und dem Presse- und Informationsamt der Bun­_


_desregierung (BPA) geprüft. Er adressiert den Bericht nach § 88 Absatz 2 BHO an die Bundes­_


_regierung. Eine besondere Verantwortung kommt dem BMDS zu, das seit seiner Einrichtung_


_für die Digital- und Datenpolitik zuständig ist und die Datenlabore koordiniert._


_Der vorliegende Bericht umfasst querschnittliche Feststellungen zu den CDO/CDS und Daten­_


_laboren, z. B. zur Infrastruktur der Datenlabore, zu IT-Dienstleistern, zur Wirtschaftlichkeit,_


_zur Informationssicherheit und zum IT-Betrieb. Seine Feststellungen zur Organisation, zur_


_datenpolitischen Gremienstruktur, zur Wirkung und zur Verstetigung der Datenlabore be­_


_schreibt der Bundesrechnungshof in einem weiteren Bericht nach § 88 Absatz 2 BHO. Fest­_


_stellungen zu einzelnen Datenlaboren hat er in gesonderten Prüfungsmitteilungen festgehal­_


_ten. Er bezeichnet die geprüften Stellen im Folgenden als „oberste Bundesbehörden“ oder_


_„Datenlabore“._


_Unter Berücksichtigung der vom BMDS mit den übrigen obersten Bundesbehörden abge­_


_stimmten Stellungnahme stellt er im Wesentlichen Folgendes abschließend fest:_

### **0.1**


_Die Bundesregierung beschloss, dass das Auswärtige Amt (AA) sein „Platform Analysis and_


_Information System“ (PLAIN) zu einer für die gesamte Bundesregierung zugänglichen Daten­_


_analyse (DA)-Plattform ausbauen soll. Im November 2024 empfahl das Bundeskanzleramt_


_den Datenlaboren, für die nächsten drei Jahre PLAIN als gemeinsame Infrastruktur zu pilo­_


_tieren. Das Bundeskanzleramt beabsichtigte, PLAIN zunächst mit jährlich 3 Mio. Euro über_


_den Einzelplan 60 zu finanzieren. Die Mehrheit der Datenlabore verfügte bis Oktober 2024_


_nicht oder nur teilweise über eine geeignete DA-Umgebung. Zwei Datenlabore konnten noch_


_im Mai 2024 überhaupt keine DA-Umgebung nutzen. Die obersten Bundesbehörden haben_


_versäumt, ihren Datenlaboren geeignete DA-Umgebungen bereitzustellen. Die Datenlabore_


_hätten sich hierzu bereits im Jahr 2021 austauschen und gemeinsame „Mindestanforderun­_


_gen“ in die jeweiligen obersten Bundesbehörden hineintragen sollen. Wie die Datenlabore_


_einschlägige Ziele der Bundesregierung erreichen wollen, wenn zwei Datenlabore über drei_


_Jahre nach dem Beschluss der Datenstrategie der Bundesregierung immer noch nicht ar­_


_beitsfähig waren, bleibt offen. Da die Datenlabore nunmehr PLAIN nutzen können, ist die_


_Wirtschaftlichkeit ihrer bisherigen „Individuallösungen“ offen._


#### **7**


_Die Datenlabore sollten prüfen, ob sich ihre DA-Umgebungen für ihre Aufgaben eignen. Dies­_


_bezügliche Anforderungen sollten sie bei Bedarf konkretisieren und erneut stellen. Die inter­_


_ministerielle Arbeitsgruppe der Datenlabore (IMAG Datenlabore) sollte „Mindestanforderun­_


_gen“ an DA-Umgebungen beschließen. Datenlabore, deren eigene DA-Umgebung diese_


_„Mindestanforderungen“ nicht erfüllt, sollten sicherstellen, dass sie eine angemessene DA-_


_Umgebung nutzen können, z. B. PLAIN. Alle Datenlabore sollten anhand einer Wirtschaftlich­_


_keitsbetrachtung (WiBe) prüfen, inwieweit sie weiterhin „Individuallösungen“ benötigen oder_


_auf PLAIN wechseln sollten. Dabei ist auch zu berücksichtigen, dass PLAIN für die einzelnen_


_Datenlabore zunächst „kostenlos“ ist. Benötigen sie im Ergebnis ihre eigene DA-Umgebung_


_nicht mehr oder können diese nicht mehr auslasten, ist diese zurückzubauen und zu verwer­_


_ten._


_Das BMDS hat erläutert, dass fast alle Datenlabore nunmehr PLAIN nutzen könnten oder_


_sich in einem „Onboarding“-Prozess befänden. Es werde PLAIN bereits im ersten Quar­_


_tal 2026 evaluieren. Der über drei Jahre angelegte Test von PLAIN diene auch dazu, Mindest­_


_anforderungen an eine DA-Umgebung zu formulieren._


_Die Datenlabore beabsichtigen, die Empfehlung zu geeigneten DA-Umgebungen und Min­_


_destanforderungen umzusetzen. Die Stellungnahme lässt offen,_


→ _inwieweit die Datenlabore anhand einer WiBe entscheiden werden, ob sie PLAIN nutzen,_


_und_


→ _ob sie ihre eigenen DA-Umgebungen zurückbauen wollen, falls sie diese nicht mehr benö­_


_tigen._


_Der Bundesrechnungshof hält an diesen Empfehlungen fest. (Tz. 2.1)_

### **0.2**


_Neun Datenlabore ließen sich für ihre Aktivitäten vom Informationstechnikzentrum Bund_


_(ITZBund) unterstützen. Die Datenlabore haben das ITZBund nicht als kundenorientierten_


_IT-Dienstleister wahrgenommen. In einem innovativen Umfeld ist nicht grundsätzlich davon_


_auszugehen, dass ein IT-Dienstleister kurzfristig neue und in der Bundesverwaltung noch_


_nicht etablierte Services anbieten kann. Dennoch hätten das ITZBund und die Datenlabore_


_besser zusammenarbeiten müssen. Die IMAG Datenlabore hätte gemeinsam mit dem_


_ITZBund prüfen sollen, warum Anfragen gescheitert sind oder das ITZBund diese abgelehnt_


_hat. Schwierigkeiten in der Zusammenarbeit mit dem ITZBund haben stattdessen dazu_


_beigetragen, dass die Datenlabore „Individuallösungen“ aufgebaut haben._


_Das BMDS sollte sich ein umfassendes Bild über bisherige Anfragen der Datenlabore beim_


_ITZBund machen und gemeinsam mit der IMAG Datenlabore und dem ITZBund prüfen, wa­_


_rum einige davon gescheitert sind. Die Datenlabore sollten sich künftig frühzeitig mit dem_


#### **8**


_ITZBund austauschen. Das ITZBund sollte prüfen, inwieweit es seine Kapazitäten und Kompe­_


_tenzen für innovative Themen weiter ausbauen kann._


_Das BMDS hat erklärt, es setze sich für eine enge und „gewinnbringende“ Zusammenarbeit_


_mit dem ITZBund ein._


_Der Bundesrechnungshof unterstreicht den Handlungsbedarf, die Zusammenarbeit mit dem_


_ITZBund effektiver und effizienter zu gestalten. Er erwartet, dass das BMDS dabei seine Emp­_


_fehlungen berücksichtigt und die IMAG Datenlabore geeignet einbindet. (Tz. 2.2)_

### **0.3**


_Alle Datenlabore beauftragten externe Dienstleister. Sie haben dabei vielfach versäumt, WiBe_


_durchzuführen. Ohne WiBe sind aber angemessene Erfolgskontrollen und somit ein „Lernen_


_aus Fehlern“ bei den teils sehr innovativen Aktivitäten der Datenlabore erschwert. Der Bun­_


_desrechnungshof hat anerkannt, dass sich einige Datenlabore seit dem Jahr 2023 darum be­_


_mühen, Beschaffungen gebündelt durchzuführen._


_Der Bundesrechnungshof hat erwartet, dass die Datenlabore künftig angemessene WiBe und_


_Erfolgskontrollen anhand überprüfbarer, mit messbaren Indikatoren unterlegter Ziele_


_durchführen. Die Datenlabore sollten ihren Prozess zur „Beschaffungsbündelung“ vorantrei­_


_ben und gemeinsam mit dem Beschaffungsamt des Bundesministeriums des Innern (BeschA)_


_bedarfsgerecht Ausschreibungen durchführen. Sie sollten künftig bei jeder Investition in die_


_eigenen DA-Umgebungen prüfen, inwieweit diese mit Blick auf PLAIN noch erforderlich und_


_wirtschaftlich wäre._


_Das BMDS bemühe sich, Effizienzpotenziale bei der Staatsmodernisierung und dem Bürokra­_


_tierückbau auszuschöpfen. Zu Erfolgskontrollen hätten sich die Datenlabore bereits ausge­_


_tauscht. Das BMDS beabsichtige, langfristig planbare Beschaffungen der Datenlabore zu_


_bündeln. Aufgrund der Rolle der Datenlabore seien aber auch „zügige“ Beschaffungen uner­_


_lässlich._


_Der Bundesrechnungshof erkennt an, dass sich die Datenlabore mittlerweile zu Erfolgskon­_


_trollen austauschen. Er erwartet, dass sie künftig die Vorgaben der BHO einhalten. Dies ist_


_erst recht in politischen Handlungsfeldern des BMDS erforderlich. Die Empfehlung des Bun­_


_desrechnungshofes zu Beschaffungen will das BMDS teilweise umsetzen. (Tz. 3)_

### **0.4**


_Die Mehrheit der Datenlabore hat gegen den Umsetzungsplan Bund 2017 (UP Bund) und_


_Vorgaben des IT-Grundschutzkompendiums des Bundesamtes für Sicherheit in der Informa­_


_tionstechnik (BSI) verstoßen. Sie haben entweder kein eigenes_


#### **9**


_Informationssicherheitskonzept (ISK) erstellt oder die jeweilige oberste Bundesbehörde hat_


_ihr ISK nicht geeignet fortgeschrieben. Zwei Datenlabore haben darüber hinaus die Ver­_


_schlusssachenanweisung (VSA) nicht eingehalten, da sie Verschlusssachen (VS) ohne gültiges_


_ISK verarbeiteten. Nur ein Datenlabor hielt den Mindeststandard des BSI zur Nutzung exter­_


_ner Cloud-Dienste ein. Die anderen Datenlabore hatten wesentliche Teile oder alle der im_


_Mindeststandard vorgesehenen Dokumente nicht erstellt._


_Die Datenlabore haben die Vorgaben des UP Bund, der VSA und des IT-Grundschutzkompen­_


_diums einzuhalten. Dafür noch fehlende ISK sind zeitnah zu erstellen oder das jeweilige ISK_


_der obersten Bundesbehörde fortzuschreiben. Dies gilt umso mehr, wenn Datenlabore VS_


_verarbeiten. Nutzen Datenlabore verwaltungsexterne Cloud-Dienste, müssen sie den Min­_


_deststandard des BSI zur Nutzung externer Cloud-Dienste einhalten. Dazu noch fehlende Do­_


_kumente sollten sie zeitnah erstellen._


_Das BMDS hat hervorgehoben, dass die Informationssicherheit zentral für staatliches Han­_


_deln sei. Es werde dazu einen Austausch der Datenlabore einleiten._


_Das BMDS lässt offen, wie die Datenlabore planen, künftig die für die Informationssicherheit_


_und den Geheimschutz relevanten Vorgaben einzuhalten. Sich dazu auszutauschen, ist_


_grundsätzlich sinnvoll. Es entbindet jedes einzelne Datenlabor aber nicht davon, fehlende ISK_


_kurzfristig zu erarbeiten oder anzupassen und die weiteren Empfehlungen umzusetzen. Der_


_Bundesrechnungshof hält an diesen fest. (Tz. 5)_

### **0.5**


_Die Datenlabore entwickelten ihre „Datenprodukte“ teils bis zur Betriebsreife. Es war teils_


_noch ungeklärt, wie die Datenlabore in übliche Prozesse der jeweiligen IT-Betriebsorganisa­_


_tion einzubinden wären. Die Datenlabore haben versäumt, Datenprodukte, die Beschäftigte_


_auch über längere Zeit nutzen sollen, geeignet an Betriebsverantwortliche außerhalb der Da­_


_tenlabore zu übergeben. Es ist nicht angemessen, dass_


→ _Behörden, für die ein Datenprodukt entwickelt wurde, sich anschließend weigern, dieses_


_zu übernehmen,_


→ _fehlende Übergaben den langfristigen Betrieb von Datenprodukten gefährden und_


→ _Beschäftigte der Datenlabore selbst Betriebsverantwortung übernehmen müssen._


_Die Datenlabore sollten darauf hinwirken, dass sie alle Datenprodukte, die Beschäftigte über_


_längere Zeit nutzen sollen, an ihre jeweils zuständige IT-Betriebsorganisation übergeben. Die_


_Datenlabore sollten gemeinsam einen Prozess erarbeiten, wie eine geordnete Betriebsüber­_


_gabe eines Datenproduktes aussehen könnte. Den Prozess sollten sie anschließend in enger_


_Abstimmung mit den Betriebsverantwortlichen ihrer jeweiligen obersten Bundesbehörden_


_umsetzen. Zu beteiligende Gremien und Beauftragte, z. B. Personalvertretungen oder Daten­_


_schutzbeauftragte, sind dabei geeignet einzubinden._


#### **10**


_Das BMDS hat die Auffassung vertreten, es sei zu prüfen, Datenprodukte bei entsprechender_


_Reife an geeignete Betriebsverantwortliche zu übergeben._


_Bloß zu prüfen, dauerhaft nutzbare Datenprodukte an Betriebsverantwortliche zu überge­_


_ben, wird den erfolgskritischen Entwicklungsaufgaben der Datenlabore nicht gerecht. Der_


_Bundesrechnungshof hält an seinen Empfehlungen fest. (Tz. 6)_

### **0.6**


_Behörden und Einrichtungen des Bundes benötigen Freiräume, um mit innovativen Techno­_


_logien wie DA/KI zu experimentieren, diese zu erproben und um daraus zu lernen. Die Daten­_


_labore sind dafür grundsätzlich geeignete Organisationseinheiten. Allerdings braucht es ein_


_wirtschaftliches, durchdachtes und überprüfbares Vorgehen, um die strategischen Ziele der_


_Bundesregierung zu erreichen und datenbasiertes Vorgehen in der Bundesverwaltung weiter_


_voranzutreiben. Der Bundesrechnungshof hat zahlreiche strukturelle Mängel bei den Daten­_


_laboren festgestellt. Er hat es für dringend erforderlich gehalten, dass die obersten Bundes­_


_behörden in ihrer jeweiligen Zuständigkeit stärker darauf hinarbeiten,_


→ _die strategischen Ziele der Bundesregierung zu erreichen und_


→ _dabei wirtschaftlich und ordnungsgemäß vorzugehen._


_Der Bundesrechnungshof hat erwartet, dass die Datenlabore dazu seine Empfehlungen be­_


_rücksichtigen. Das nunmehr zuständige BMDS sollte diesen Prozess eng begleiten und koor­_


_dinieren. Es könnte dazu einen „Leitfaden für Datenlabore oberster Bundesbehörden“ erstel­_


_len und von der IMAG Datenlabore beschließen lassen._


_Das BMDS hat dargestellt, die Datenlabore sollten wirkungsvolles staatliches Handeln durch_


_eine evidenzbasierte Entscheidungsfindung stärken. Sie arbeiteten eng zusammen und hät­_


_ten zahlreiche Mehrwerte generiert. Fachliche Bedarfe und Eigenheiten sowie strategische_


_und konzeptionelle Fragen der obersten Bundesbehörden beeinflussten dabei die Umsetz­_


_barkeit und Wirksamkeit der Empfehlungen. Die Datenlabore hätten aus den Empfehlungen_


_konkrete Maßnahmen abgeleitet._


_Der Bundesrechnungshof erkennt das zentrale Ziel der Datenlabore an. Um dieses zu errei­_


_chen, sollten die obersten Bundesbehörden seine Empfehlungen beachten und nicht implizit_


_auf das Ressortprinzip verweisen. „Konkrete Maßnahmen“ kann der Bundesrechnungshof in_


_der Stellungnahme des BMDS kaum ausmachen. Im Bereich des datenbasierten Verwal­_


_tungshandelns besteht seit Jahren dringender Handlungsbedarf. Die Bundesregierung hat_


_dazu in ihrer „Modernisierungsagenda für Staat und Verwaltung (Bund)“ (Modernisierungs-_


_agenda) bekundet, die notwendige Grundlagenarbeit an ihren Datenbeständen zu priorisie­_


_ren. Für den Bundesrechnungshof bleibt offen, wie sie dies ohne geeignet ausgestattete, da­_


_tenschutzkonform, sicher und wirtschaftlich arbeitende Datenlabore umsetzen will. Die_


_Datenlabore sollten der Bundesverwaltung als Vorbild vorangehen und über ihre_


#### **11**


_wegweisende Zusammenarbeit unter gemeinsamen Standards, Prozessen und Strukturen_


_aufzeigen, wie zeitgemäßes Verwaltungshandeln aussehen könnte._


_Der Bundesrechnungshof hält weiterhin an seiner Empfehlung zu einem „Leitfaden für Da­_


_tenlabore oberster Bundesbehörden“ fest. Er beabsichtigt, den weiteren Aufbau und die Ver­_


_stetigung der Datenlabore in den kommenden Jahren eng zu begleiten. (Tz. 7)_


#### **12**


## **1 Vorbemerkung**

### **1.1 Datenanalyse, künstliche Intelligenz und** **Datenmanagement**

Daten bilden seit jeher die Grundlage für Entscheidungen. Sie enthalten Informationen,


die die öffentliche Verwaltung dazu nutzen kann, Geschehenes zu überprüfen oder


neue Erkenntnisse [1] zu gewinnen. Verfahren der DA und der künstlichen Intelligenz (KI)


sind Ansätze, um solche Informationen aus Daten zu gewinnen. [2] Die Bundesregierung


betrachtet Daten inzwischen als eine strategische Ressource, die einen signifikanten


Beitrag zur Sicherung des Wohlstandes in Deutschland leisten können. [3] Sie bewertet


Daten daher als Schlüsselressource und sieht darin ein enormes „Innovationspotential“


für die deutsche Wirtschaft, Verwaltung und Gesellschaft.


Unter das Datenmanagement (DM) fallen alle Verfahren und organisatorischen Tätig­


keiten, die dazu dienen, Daten aufzubereiten und in Geschäftsprozessen bereitzustel­


len. [4] Herausforderungen sind dabei insbesondere die Datenqualität und -verfügbar­


keit.

### **1.2 Datenstrategie der Bundesregierung**


Im Januar 2021 beschloss die Bundesregierung eine Datenstrategie. [5] Mit dieser beab­


sichtigte sie, die „innovative und verantwortungsvolle Datenbereitstellung und Daten­


nutzung […] signifikant [zu] erhöhen“.


Dies wollte sie anhand von vier Handlungsfeldern erreichen:


1. Datenbereitstellung verbessern und Datenzugang sichern,


2. verantwortungsvolle Datennutzung befördern und Innovationspotenziale heben,


3. Datenkompetenz erhöhen und Datenkultur etablieren und


4. den Staat zum Vorreiter machen.


………………………………………………………………………………………………………………………………………………………………………………………………………

1 Auch über mögliche zukünftige Entwicklungen sowie darüber, wie sich Entscheidungen auswirken könnten.

2 Zu den DA-Verfahren zählen sowohl beschreibende Auswertungen von Datenbeständen als auch „explorative“ An­
sätze. Diese können zu neuen Erkenntnissen führen. KI-Verfahren gehen noch darüber hinaus: Hier handelt es sich
um Verfahren, die (weitgehend) selbständig „lernend“ Informationen aus Daten ziehen können. Diese Informationen
können Behörden und Unternehmen z. B. bei der Entscheidungsunterstützung und bei Prognosen von Geschäftsund Verwaltungsvorgängen nutzen.

3 [Eckpunkte einer Datenstrategie der Bundesregierung, S. 1., zuletzt abgerufen am 3. März 2026.](https://www.bundesregierung.de/resource/blob/974430/1693626/60b196d5861f71cdefb9e254f5382a62/2019-11-18-pdf-datenstrategie-data.pdf?download=1)

4 Peter Ernst Tiemeyer (Hrsg.): Handbuch IT-Management, 6. Auflage, Carl Hanser Fachbuchverlag, München, S. 216.

5 [Pressemitteilung zur Datenstrategie, zuletzt abgerufen am 3. März 2026.](https://www.bundesregierung.de/breg-de/aktuelles/datenstrategie-beschlossen-1842786)


#### **13**


### **1.3 Chief Data Scientists und Datenlabore**

Prüfungsgegenstand waren die CDO/CDS sowie die Datenlabore [6] der obersten Bundes­


behörden.


Im Handlungsfeld 4 ihrer Datenstrategie („Den Staat zum Vorreiter machen“) sah die


Bundesregierung jeweils als „wesentliche Maßnahme“ vor, dass


→ alle Bundesministerien CDS oder vergleichbare Rollen (z. B. CDO) einführen. [7] Diese


sollten „mit einem Kernteam von Daten-Analystinnen und -Analysten zusammenar­


beiten“ [8] . „Die Teammitglieder sollten eine nachgewiesene Kompetenz im Bereich


Data Science und Statistik besitzen.“ [9]


→ alle Bundesministerien interne Datenlabore einrichten. [10]


Für diese Maßnahmen war [11] das Bundeskanzleramt federführend [12] . Inzwischen haben


alle Bundesministerien [13], das Bundeskanzleramt und das BPA Datenlabore eingerich­


tet. [14]


Nach Organisationserlass des Bundeskanzlers vom 6. Mai 2025 ist das BMDS für die Di­


gital- und Datenpolitik zuständig. Es hat auch die Federführung der ressortübergreifen­


den Gremien zu diesen Themen übernommen.


Die/der **CDO** ist für das DM der Behörde verantwortlich. Dazu gehört u. a., eine interne


Data Governance [15] zu entwickeln und umzusetzen. [16]


………………………………………………………………………………………………………………………………………………………………………………………………………

6 Die Datenstrategie der Bundesregierung enthielt keine allgemeine Definition eines Datenlabors. Ein Datenlabor ist in
der Regel eine Organisationseinheit innerhalb einer Behörde oder eines Unternehmens, die u. a. KI/DA-Verfahren
und weitere neue Technologien erprobt und mit einem agilen, nutzenorientierten Ansatz Datenprodukte entwickelt,
z. B. Dashboards. Datenlabore sollen datengetriebene Entscheidungen ermöglichen und die Datenkompetenz in
Behörden und Unternehmen erhöhen.


7 Maßnahme „Chief Data Science Officer für das Bundeskanzleramt und alle Bundesministerien“ aus der Datenstrate­
gie der Bundesregierung.

8 Ebenda.


9 Ebenda.

10 Maßnahme „Einrichtung von Datenlaboren im Bundeskanzleramt und bei den Bundesministerien“ aus der Daten­

strategie der Bundesregierung.

11 Mit Organisationserlass vom 6. Mai 2025 übertrug der Bundeskanzler die Zuständigkeit für die Datenpolitik an das

neu gebildete BMDS. Der Bundesrechnungshof verwendet in diesem Bericht nach § 88 Absatz 2 BHO stets die Be­
zeichnungen der Bundesministerien nach dem Organisationserlass.

12 Zunächst gemeinsam mit dem AA, dem Bundesministerium des Innern, dem Bundesministerium für Forschung,

Technologie und Raumfahrt, dem Bundesministerium für Umwelt, Klimaschutz, Naturschutz und nukleare Sicher­
heit, dem Bundesministerium der Verteidigung und dem Bundesministerium für wirtschaftliche Zusammenarbeit
und Entwicklung. Ab August 2023 war das Bundeskanzleramt alleinig federführend.

13 Außer BMDS, da sich dieses im Aufbau befindet.

14 Antwort der Bundesregierung auf eine Kleine Anfrage der Fraktion CDU/CSU, Bundestagsdrucksache 20/9821 vom

11. Dezember 2023.

15 Die Data Governance beschreibt u. a. Gesetze, Verordnungen, Standards, interne Regelungen und Organisations­

strukturen bzgl. des DM in Behörden oder Unternehmen.

16 Gemäß dem Glossar zur Datenstrategie der Bundesregierung.


#### **14**


Die/der **CDS** hingegen


→ ist dafür verantwortlich,


       - Datenquellen in einer Organisation zu erschließen und auszuwerten,


       - interne und externe Daten zu analysieren,


       - Dashboards und andere Visualisierungen zu erstellen,


→ kann auch das DM verantworten,


→ arbeitet in einer Organisation unabhängig [17] und


→ arbeitet eng mit der Open-Data-Koordinatorin [18] oder dem Open-Data-Koordinator


(ODK) sowie der/dem (behördlichen) Datenschutzbeauftragten zusammen. [19]


Im August 2023 entwickelte die Bundesregierung ihre Datenstrategie weiter. [20] Dem­


nach waren


→ die Datenlabore als OE in den Bundesministerien bis zum Jahr 2025 zu verstetigen,


→ die CDO/CDS sowie die ODK in den Datenlaboren verortet und


→ die Datenlabore auch für den „Datenatlas“ [21], den „Datenpool“ [22] und gemeinsam mit


weiteren Organisationseinheiten [23] für den Einsatz von sogenannten „großen Sprach­


modellen“ [24] (LLM) zuständig.


Gemäß ihrer Digitalstrategie wollte sich die Bundesregierung im Jahr 2025 daran „mes­


sen lassen, ob […] alle Ressorts Datenlabore etabliert und verstetigt haben“ [25] . Die Da­


tenlabore sollten insbesondere „geeignete Werkzeuge und Ressourcen“ [26] zur DA be­


reitstellen.


Im Oktober 2025 beschloss die Bundesregierung ihre Modernisierungsagenda. [27] Die


darin beschriebenen „Hebelprojekte“ und Maßnahmen setzen vielfach voraus, dass


entsprechende Daten vorliegen sowie dazugehörige Kompetenzen bestehen, u. a.,


wenn Behörden Prozesse


→ automatisieren [28] oder


→ mittels KI „spürbar erleichtern“ [29] sollen.


………………………………………………………………………………………………………………………………………………………………………………………………………

17 Gemäß dem Glossar zur Datenstrategie der Bundesregierung. Ob es sich dabei um eine weisungsfreie Tätigkeit han­

delt oder um eine lediglich „fachliche“ Unabhängigkeit des CDS, legt die Datenstrategie nicht fest.

18 Der oder die ODK wirkt als zentrale Ansprechpartnerin oder -partner der jeweiligen Behörde auf die Identifizierung,

Bereitstellung und Weiterverwendung offener Daten der Behörde hin (§ 12a EGovG).

19 Gemäß dem Glossar zur Datenstrategie der Bundesregierung.

20 [Pressemitteilung zur Weiterentwicklung der Datenstrategie, zuletzt abgerufen am 3. März 2026.](https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2023/08/nationale-datenstrategie.html)

21 Maßnahme „Datenatlas der Bundesverwaltung“ aus der Datenstrategie der Bundesregierung.

22 Maßnahme „Gemeinsamer interner Datenpool der Bundesbehörden“ aus der Datenstrategie der Bundesregierung.

23 Z. B. dem Beratungszentrum für KI.

24 Large Language Models wie z. B. ChatGPT von OpenAI.

25 Digitalstrategie der Bundesregierung, Aktualisierung vom 25. April 2023, S. 46.

26 Ebenda.

27 [Modernisierungsagenda für Staat und Verwaltung (Bund), zuletzt abgerufen am 3. März 2026.](https://bmds.bund.de/fileadmin/BMDS/Dokumente/Modernisierungsagenda_barrierefrei-neu.pdf)

28 Z. B. Maßnahme 1.2 im Handlungsfeld V „Effiziente Bundesverwaltung“ der Modernisierungsagenda.

29 Modernisierungsagenda, S. 36.


#### **15**


Der Koalitionsvertrag für die 21. Legislaturperiode sieht dazu u. a. vor, Daten besser zu


nutzen und die Datenkompetenz zu stärken. [30] Die Bundesregierung beabsichtigt,


hierzu „die notwendige Grundlagenarbeit an den Datenbeständen der Bundesverwal­


tung“ [31] zu priorisieren, „damit der Einsatz von KI auf einer soliden Datenbasis erfolgen


kann“ [32] . Die Datenprodukte der Datenlabore sollen zu „Blaupausen für die zentrale


oder dezentrale Nachnutzung“ [33] werden.

### **1.4 Datenpolitische Gremienstruktur**


Die Bundesregierung richtete in der letzten Legislaturperiode im Bereich der Datenpo­


litik eine mehrstufige Gremienstruktur ein.


Oberstes Gremium war bis zum Beginn der aktuellen Legislaturperiode die digitalpoliti­


sche St-Runde). Unter der Leitung des Chefs des Bundeskanzleramtes tagte sie mehr­


fach im Jahr. Sie hat insbesondere über strategische Themen der Datenpolitik entschie­


den. Die digitalpolitische St-Runde erteilte u. a. [34] Aufträge an die IMAG Datenlabore.


In der IMAG Datenlabore waren grundsätzlich die CDO/CDS des Bundeskanzleramtes,


der Bundesministerien und des BPA vertreten [35] . Diese tauschten sich seit August 2021


zu strategischen Themen von ressortübergreifender Bedeutung für die Datenlabore


aus. [36] Die IMAG Datenlabore tagte bis zu sechsmal im Jahr. Das Bundeskanzleramt or­


ganisierte und leitete die Sitzungen. [37] Neben der IMAG Datenlabore organisierte das


Bundeskanzleramt weitere Austauschformate der CDO/CDS [38] .


Auf Arbeitsebene haben die Datenlabore ein „Peer-to-Peer“-Netzwerk gebildet, um Wis­


sen auszutauschen und gemeinsam Lösungen zu erarbeiten. In monatlichen Treffen


und sogenannten „aktiven Themenclustern“ erörterten die Teilnehmenden ressort­


übergreifend u. a. folgende Themen:


………………………………………………………………………………………………………………………………………………………………………………………………………

30 [Koalitionsvertrag zwischen CDU, CSU und SPD „Verantwortung für Deutschland“, Kapitel 2.2, Zeilen 1858 ff, zuletzt](https://www.koalitionsvertrag2025.de/sites/www.koalitionsvertrag2025.de/files/koav_2025.pdf)

abgerufen am 3. März 2026.

31 Modernisierungsagenda, S. 36.

32 Ebenda.


33 Ebenda, S. 31.

34 Die digitalpolitische St-Runde erteilte auch Aufträge an die für die jeweiligen datenpolitischen Themen zuständigen

Bundesministerien.

35 Einige oberste Bundesbehörden entsendeten in die IMAG Datenlabore ergänzend Vertreter der Federführung des

jeweiligen Datenlabors. Seit der 14. Sitzung am 10. April 2024 ist auch der Bundesrechnungshof in der IMAG Daten­
labore vertreten.

36 Die IMAG Datenlabore hat eine Unterarbeitsgruppe „LLM-Applikationen in der Bundesverwaltung“ eingerichtet. Die

Unterarbeitsgruppe sollte
→ eine „Shortlist“ von LLM-Applikationen für ressortübergreifende Nutzung erstellen,
→ LLM-Applikationen bewerten, beauftragen und ggf. selbstständig umsetzen und
→ Anwendungsfälle für LLM koordinieren.

37 Ab der 23. Sitzung der IMAG Datenlabore am 17. September 2025 übernahm das BMDS diese Aufgabe.

38 U. a. einen Jour Fixe alle zwei Wochen: die CDO/CDS besprechen dort z. B. Themen, die nicht in die IMAG Datenla­

bore eskaliert werden müssen und bereiten die IMAG Datenlabore vor. Dieser Jour Fixe fand seit Ende 2023 statt.


#### **16**


→ Data Governance,


→ Infrastruktur,


→ Daten- und KI-Kompetenz und


→ Natural Language Processing [39] .


In „virtuellen Themenclustern“ teilte das „Peer-to-Peer“-Netzwerk Recherchen und sam­


melte Informationen u. a. zu folgenden Themen:


→ Beschaffung,


→ Finanzierung und


→ Konzeption sowie Organisation.

### **1.5 Querschnittliche Erhebung des** **Bundesrechnungshofes**


Für diese Prüfung hat der Bundesrechnungshof dem Bundeskanzleramt, den Bundes­


ministerien und dem BPA einen Fragebogen übersandt. Er erhielt von allen geprüften


Stellen Antworten, die er für diesen Bericht auswertete. [40] Der Begriff „die/alle Datenla­


bore“ [41] beinhaltet die Antworten aller 17 befragten Datenlabore.

## **2 Infrastruktur und IT-Dienstleister**

### **2.1 Infrastruktur**

###### **2.1.1 Sachverhalt**


Die Anforderungen an eine für Datenlabore geeignete DA-Umgebung unterscheiden


sich wesentlich von Anforderungen an in der öffentlichen Verwaltung übliche „Büroar­


beitsplätze“. Darunter fallen u. a.


→ der Zugriff auf eine Entwicklungsumgebung,


→ die Möglichkeit, entwickelte Anwendungen (sogenannte „Datenprodukte“) bereitzu­


stellen und für Beschäftigte aus dem jeweiligen Hausnetz heraus verfügbar zu ma­


chen und


………………………………………………………………………………………………………………………………………………………………………………………………………

39 Verarbeitung natürlicher Sprache.

40 Insgesamt 17 Fragebögen. Prozentangaben in den folgenden Abbildungen und dem Text sind gerundet dargestellt.

Insofern kann es bei Summen zu geringfügigen Abweichungen kommen.

41 Also die Antworten des Bundeskanzleramtes, der Bundesministerien ohne BMDS und des BPA.


#### **17**


→ in einer Umgebung sowohl öffentlich verfügbare Daten aus dem Internet als auch

nach VSA [42] als „Verschlusssache – NUR FÜR DEN DIENSTGEBRAUCH“ (VS-NfD) einge­


stufte Daten verarbeiten zu können.


Im Jahr 2021 stellte die Bundesregierung fest, auf Infrastrukturebene sei „vor allem


eine grundlegende Konsolidierung und Modernisierung notwendig, deren Umsetzung


beschleunigt werden muss“ [43] . Sie entschied daher, dass die Plattform PLAIN des AA „als


Blaupause und Anbieter [...] für die Bundesregierung insgesamt dienen“ [44] könne.


PLAIN solle „als Vorlage für eine ressortübergreifende Dateninfrastruktur zu einer für


die gesamte Bundesregierung zugänglichen Datenanalyseplattform ausgebaut wer­


den“ [45] . „Bereits bestehende Infrastrukturen [seien] in geeigneter Form einzubinden,


um Doppelarbeiten zu vermeiden.“ [46]


Laut Bundeskanzleramt sei eine technische Infrastruktur zur Entwicklung und zum Be­


trieb datengetriebener Anwendungen Grundlage für die Arbeit der Datenlabore. Bis


November 2024 habe allerdings eine einheitliche Infrastruktur gefehlt. Dies habe dazu


geführt, dass einzelne Datenlabore noch auf Laptops entwickelten. Eine gemeinsame


Infrastruktur sei unerlässlich, da sie


→ die professionelle Arbeitsfähigkeit aller Datenlabore herstelle,


→ Aufwände für die Nachnutzung von Datenprodukten reduziere, die ein einzelnes Da­


tenlabor entwickelt hat, und


→ die Arbeit an gemeinsamen Datenprojekten vereinfache, z. B. der Maßnahme „Ge­


meinsamer interner Datenpool der Bundesbehörden“ (Datenpool) [47] .


Der Chef des Bundeskanzleramtes bat die Datenlabore im Februar 2024 [48], ihre Anwen­


dungsfälle und Infrastruktur stärker zu konsolidieren. Die Datenlabore wählten daher


bis November 2024 in einem strukturierten Prozess PLAIN als gemeinsame Infrastruk­


tur aus. Nach drei Jahren soll die IMAG Datenlabore PLAIN evaluieren. [49] PLAIN entspre­


che den technischen Anforderungen der Datenlabore. Das Bundeskanzleramt beab­


sichtigte, die gemeinsame Infrastruktur für alle Datenlabore zunächst mit jährlich


3 Mio. Euro über den Einzelplan 60 zu finanzieren. [50]


………………………………………………………………………………………………………………………………………………………………………………………………………

42 Allgemeine Verwaltungsvorschrift zum materiellen Geheimschutz.

43 Datenstrategie der Bundesregierung, S. 50.

44 Ebenda, S. 61.

45 Ebenda, S. 60.

46 Ebenda.

47 Maßnahme „Gemeinsamer interner Datenpool der Bundesbehörden“ aus der Datenstrategie der Bundesregierung,

vgl. Tz. 1.3.

48 Bei der sogenannten „Sonder-IMAG“ am 13. Februar 2024.

49 Zwischenzeitlich sei darauf zu achten, zu entwickelnde Datenprodukte nicht z. B. aufgrund technischer Abhängigkei­

ten langfristig an PLAIN zu binden. Es müsse möglich bleiben, die Datenprodukte auf andere Infrastrukturen zu mig­

rieren.

50 Kapitel 6002 Titel 532 05, „Verstärkung von Ausgaben zur Fortführung der Datenlabore“.


#### **18**


Der Bundesrechnungshof befragte die Datenlabore, welche Anforderungen sie an ihre


eigene DA-Umgebung gestellt hatten. Zwei Datenlabore hatten keine Anforderungen


gestellt.


Die Mehrheit der Datenlabore meldete dem Bundesrechnungshof, sie verfügten nicht


oder nur teilweise über eine geeignete DA-Umgebung (vgl. Abbildung 1). Unter den Da­


tenlaboren, die nicht oder nur über eine teilweise geeignete Umgebung verfügten, be­


fanden sich beide Datenlabore, die vorher keine Anforderungen gestellt hatten.


Abbildung 1

#### **DA-Umgebungen nur teilweise geeignet**


Die Mehrheit der Datenlabore verfügte nicht über eine geeignete eigene DA-Umgebung.













Grafik: Bundesrechnungshof. Quelle: Auswertung von Erhebungsdaten.


Gemeinsame „Mindestanforderungen“ an ihre DA-Umgebungen hatten die Datenla­


bore nicht erarbeitet.


Das Datenlabor des Bundeskanzleramtes erhob im Mai 2024, über welche DA-Umge­


bungen die Datenlabore verfügten. Es stellte fest, dass zwei Datenlabore noch über­


haupt keine DA-Umgebung nutzen konnten. 71 % der Datenlabore hatten bereits eine


eigene DA-Umgebung oder diese beauftragt.


Das Bundeskanzleramt stellte im Mai 2024 fest, das gemeinsame Teilen von Daten, das


Erarbeiten und Ausrollen von Anwendungsfällen über Ressortgrenzen hinweg sei nicht


gegeben. Dies bremse auch andere Vorhaben wie den Datenpool. 56 % der Datenla­


bore bezeichneten ihre eigene DA-Umgebung oder eine fehlende gemeinsame Infra­


struktur als Problem.


Dem Bundesrechnungshof meldete ein Datenlabor, seine DA-Umgebung bestehe aus


drei ausgesonderten Laptops. Auch ein übliches Visualisierungswerkzeug könne dieses


Datenlabor nicht nutzen, da die Ressourcen der IT ausgeschöpft seien.


Das Bundeskanzleramt sah hier die Problematik von Individuallösungen in den Res­


sorts. Aufgrund der Heterogenität der IT-Architekturen sowie der Anforderungen u. a.


#### **19**


an den Schutzbedarf hielt das Bundeskanzleramt es nicht für realistisch, Individuallö­


sungen abzubauen.

###### **2.1.2 Würdigung**


Die jeweiligen obersten Bundesbehörden haben versäumt, ihren Datenlaboren geeig­


nete DA-Umgebungen bereitzustellen. Bei den Datenlaboren, die dazu keine Anforde­


rungen gestellt haben, liegt das Versäumnis beim jeweiligen Datenlabor: Ohne Anfor­


derungen an eine DA-Umgebung zu stellen, ist es wenig überraschend, dass sich die


dann bereitgestellte Umgebung nicht für das Datenlabor eignet. Hier wäre ein frühzei­


tiger Austausch der Datenlabore bereits im Jahr 2021 erforderlich gewesen, um einheit­


lich vorzugehen und „Mindestanforderungen“ an DA-Umgebungen über die IMAG Da­


tenlabore in die jeweiligen obersten Bundesbehörden hineinzutragen.


Wie die Datenlabore die Ziele der Bundesregierung erreichen wollen, wenn über drei


Jahre nach dem Beschluss der Datenstrategie


→ ein gemeinsames Teilen oder Arbeiten an Anwendungsfällen immer noch nicht mög­


lich war und


→ zwei Datenlabore immer noch nicht arbeitsfähig waren,


bleibt offen. Drei ausgesonderte Laptops sind keine angemessene DA-Umgebung.


Der Bundesrechnungshof hat anerkannt, dass sich das Bundeskanzleramt darum be­


müht hat, „Individuallösungen“ abzubauen. Die Datenlabore können nunmehr das


„kostenlose“ PLAIN nutzen (vgl. Tz. 2.1.1). Daher bleibt offen, inwieweit ihre bisherigen


DA-Umgebungen noch wirtschaftlich sind.

###### **2.1.3 Empfehlung**


Die Datenlabore sollten noch einmal prüfen,


→ ob sich ihre eigenen DA-Umgebungen für ihre Aufgaben eignen und


→ inwieweit ihre Anforderungen in den jeweiligen obersten Bundesbehörden bekannt


sind.


Bei Bedarf wären die Anforderungen zu konkretisieren und erneut zu stellen. Die Da­


tenlabore sollten sich innerhalb der IMAG Datenlabore auf „Mindestanforderungen“ an


DA-Umgebungen einigen und diese beschließen.


Datenlabore, deren eigene DA-Umgebung die „Mindestanforderungen“ nicht erfüllt,


sollten zeitnah sicherstellen, dass sie eine angemessene DA-Umgebung nutzen kön­


nen. Dies könnte z. B. PLAIN sein.


#### **20**


Alle Datenlabore sollten anhand einer WiBe kritisch prüfen, inwieweit sie


→ vollständig auf PLAIN wechseln sollten,


→ neben PLAIN noch ihre „Individuallösung“ benötigen oder


→ PLAIN nicht nutzen und stattdessen an ihrer eigenen DA-Umgebung festhalten wol­


len.


Bei diesen Handlungsalternativen ist geeignet zu berücksichtigen, dass PLAIN für ein­


zelne Datenlabore zunächst kostenlos ist. Eine diesbezügliche WiBe ist auch dann zu


erstellen, wenn für die eigene DA-Umgebung bereits eine vor November 2024 gefer­


tigte WiBe vorliegen sollte. [51] Benötigen Datenlabore im Ergebnis ihre eigene DA-Umge­


bung nicht mehr oder können diese nicht mehr auslasten, ist diese zurückzubauen und


zu verwerten. Dadurch entstehende Einnahmen oder Ausgaben wären in der WiBe zu


berücksichtigen. Die Datenlabore sollten auch gemeinsame Datenprojekte wie den Da­


tenpool auf PLAIN umsetzen.

###### **2.1.4 Stellungnahme**


Das BMDS hat bestätigt, dass eine geeignete DA-Umgebung für die effektive Arbeit der


Datenlabore „unabdingbar“ sei. Fast alle Datenlabore könnten nunmehr PLAIN nutzen


oder befänden sich im dafür erforderlichen „Onboarding“-Prozess. Das BMDS werde


PLAIN bereits im ersten Quartal 2026 evaluieren. Anhand der Ergebnisse werde es


PLAIN strategisch ausrichten sowie weiter ausstatten. Der über drei Jahre angelegte


Test von PLAIN mit mehreren Evaluationen diene auch dazu, Mindestanforderungen an


eine DA-Umgebung zu formulieren. Das BMDS werde u. a. Sicherheitsaspekte prüfen.

###### **2.1.5 Abschließende Würdigung**


Die Datenlabore beabsichtigen, die Empfehlung des Bundesrechnungshofes zu geeig­


neten DA-Umgebungen und dazugehörigen Mindestanforderungen umzusetzen.


Die Stellungnahme lässt im Übrigen offen, inwieweit die Datenlabore anhand einer


WiBe entscheiden werden, ob sie PLAIN nutzen. Ebenso hat das BMDS nicht zugesagt,


dass die Datenlabore ihre eigenen DA-Umgebungen zurückbauen werden, falls sie


diese künftig nicht mehr benötigen sollten. Der Bundesrechnungshof hält an diesen


Empfehlungen weiterhin fest.


………………………………………………………………………………………………………………………………………………………………………………………………………

51 Die Entscheidung des Bundeskanzleramtes für PLAIN stellt einen „geeigneten Fall“ nach VV Nummer 2.2 zu § 7 BHO

dar, da sie die Rahmenbedingungen für eigene DA-Umgebungen der Datenlabore wesentlich verändert hat.


#### **21**


### **2.2 IT-Dienstleister**

###### **2.2.1 Sachverhalt**

Die Datenlabore ließen sich für ihre Aktivitäten von IT-Dienstleistern der Bundesverwal­


tung unterstützen. Neun Datenlabore nutzten dafür das ITZBund.


Ein Datenlabor stellte fest, Bedarfsträger erlebten das ITZBund oft als schwerfälligen


Apparat und nicht als kundenorientierten IT-Dienstleister. Das ITZBund verwalte und


arbeite in komplizierten Prozessen, anstatt Bedarfsträger aktiv zu beraten und durch


den Prozess zu begleiten. Datenlabore nannten als Probleme z. B. Grenzen innerhalb


der (vollkonsolidierten) IT und fehlende Leistungsfähigkeit von Dienstleistern.
















































#### **22**


#### **23**


###### **2.2.2 Würdigung**

Die Datenlabore haben das ITZBund als schwerfälligen Apparat und nicht als kunden­


orientierten IT-Dienstleister wahrgenommen. Ursächlich hier war u. a., dass es


→ ein Datenlabor nicht im gewünschten „Full Service“, sondern mit üblichen Büroar­


beitsplätzen ausstattete.


→ Datenlaboren zu einer im ITZBund im Aufbau befindlichen DA-Umgebung keine Aus­


künfte gab und Angebotsaufforderungen unbegründet ablehnte.


→ einem Datenlabor eine kostenpflichtige Datenbank trotz voriger Zusage nicht bereit­


stellen konnte.


→ eine VS-NfD Freigabe für eine in eigener Hoheit befindliche DA-Umgebung weder


eigenständig noch fristgerecht durchführen konnte.


In einem innovativen und sich schnell wandelnden Umfeld ist nicht grundsätzlich da­


von auszugehen, dass ein IT-Dienstleister kurzfristig neue und in der Bundesverwal­


tung noch nicht etablierte Services anbieten kann. Dennoch hätten das ITZBund und


die Datenlabore besser zusammenarbeiten müssen. Die IMAG Datenlabore hätte ge­


meinsam mit dem ITZBund prüfen sollen, warum so viele Anfragen der Datenlabore


gescheitert sind oder das ITZBund diese abgelehnt hat. Die Schwierigkeiten in der Zu­


sammenarbeit mit dem ITZBund haben stattdessen dazu beigetragen, dass die Daten­


labore „Individuallösungen“ aufgebaut haben, meist innerhalb der IT ihrer jeweiligen


obersten Bundesbehörde.


#### **24**


###### **2.2.3 Empfehlung**

Das BMDS sollte sich ein umfassendes Bild über die bisherigen Anfragen der Datenla­


bore beim ITZBund machen. Anschließend hat es gemeinsam mit der IMAG Datenla­


bore und dem ITZBund zu prüfen, warum einige davon gescheitert sind. Für künftige


Anwendungsfälle abseits der gemeinsamen Infrastruktur sollten die Datenlabore sich


koordinieren und frühzeitig mit dem ITZBund austauschen. Das ITZBund sollte prüfen,


inwieweit es seine Kapazitäten und Kompetenzen für innovative Themen weiter aus­


bauen kann.

###### **2.2.4 Stellungnahme**


Das BMDS hat erklärt, es setze sich für eine enge und „gewinnbringende“ Zusammen­


arbeit mit dem ITZBund ein. Es wolle hier mit hoher Priorität Effizienz- und Effektivitäts­


potentiale realisieren.

###### **2.2.5 Abschließende Würdigung**


Der Bundesrechnungshof unterstreicht den Handlungsbedarf, die Zusammenarbeit


der Datenlabore mit dem ITZBund effektiver und effizienter zu gestalten. Er erwartet,


dass das BMDS dabei seine Empfehlungen berücksichtigt und die IMAG Datenlabore


geeignet einbindet.

## **3 Wirtschaftlichkeit**

### **3.1 Sachverhalt**

###### **3.1.1 Einsatz externer Dienstleister**


Nach § 7 BHO sind für jede finanzwirksame Maßnahme in der Bundesverwaltung ange­


messene Wirtschaftlichkeitsuntersuchungen durchzuführen. Eine Wirtschaftlichkeits­


untersuchung dient dabei auch als Planungsinstrument. Für IT-Vorhaben sind die An­


forderungen an eine WiBe gemäß den Empfehlungen [52] des damaligen Beauftragten


der Bundesregierung für Informationstechnik zu berücksichtigen. Abhängig vom


………………………………………………………………………………………………………………………………………………………………………………………………………

52 Fachkonzept WiBe 5.0 „Konzept zur Durchführung von Wirtschaftlichkeitsbetrachtungen in der Bundesverwaltung,

insbesondere beim Einsatz der IT“.


#### **25**


zeitlichen und inhaltlichen Umfang der Maßnahmen sind weitere Versionen der WiBe


als begleitende Erfolgskontrollen während der Realisierung durchzuführen. [53]


Alle Datenlabore setzten externe Dienstleister ein. Die Datenlabore schlossen dafür bis


einschließlich Juni 2024 insgesamt 88 Verträge mit einem Auftragsvolumen von


49,9 Mio. Euro ab. Der Bundesrechnungshof wertete aus, zu welchen ihrer Aktivitäten


mit externen Dienstleistern die Datenlabore eine WiBe [54] erstellt hatten (vgl. Abbildung


2). Er stellte fest, dass 29 % der Datenlabore für alle Aktivitäten WiBe anfertigten. 24 %


der Datenlabore fertigten für keine ihrer Aktivitäten eine WiBe.


Abbildung 2

#### **WiBe für Aktivitäten der Datenlabore**


Nur wenige Datenlabore erstellten für sämtliche Aktivitäten mit externen Dienstleistern eine


WiBe.













Grafik: Bundesrechnungshof. Quelle: Auswertung von Erhebungsdaten.

###### **3.1.2 Beschaffungen**


Die Datenlabore planten, im September 2023 einen gemeinsamen Workshop mit dem


BeschA durchzuführen. Ziel war es, gemeinsame Bedarfe zu identifizieren und perspek­


tivisch über Rahmenvereinbarungen abzudecken. Die Datenlabore führten den Work­


shop nicht durch.


Im Dezember 2023 planten die Datenlabore erneut, ihre Beschaffungen künftig zu bün­


deln. Das Datenlabor des Bundeskanzleramtes führte dazu eine Abfrage unter den Da­


tenlaboren durch. Ziel war es,


→ die Bedarfe der Datenlabore zusammenzuführen und zu bündeln sowie


→ in einem nächsten Schritt gemeinsam(e) Ausschreibung(en) durchzuführen, um


→ gemeinsam(e) Rahmenvereinbarung(en) zu schließen.


………………………………………………………………………………………………………………………………………………………………………………………………………

53 Begleitende Erfolgskontrollen umfassen eine Zielerreichungs-, Wirkungs- und Wirtschaftlichkeitskontrolle; VV Num­

mer 2.2 zu § 7 BHO.

54 Der Bundesrechnungshof prüfte nicht die Qualität der WiBe.


#### **26**


Dieses Vorgehen ermögliche Kostensynergien. Neun Datenlabore antworteten auf die


Abfrage. Im Februar 2024 führten die Datenlabore dazu einen Workshop mit dem Be­


schA durch. [55] Ihre Beschaffungen haben die Datenlabore daraufhin nicht gebündelt.


Die Datenlabore beschafften bis einschließlich Juni 2024 Hard- und Software für


10,8 Mio. Euro. Für mehr als 95 % davon war weniger als die Hälfte der Datenlabore


verantwortlich. Zehn Datenlabore gaben insgesamt weniger als 5 % dieser Summe aus.


Drei Datenlabore beschafften keinerlei Hard- oder Software.


Einzelne Datenlabore beschafften dabei z. B.


→ teils nicht genutzte Lizenzen und Server für knapp 3,5 Mio. Euro oder


→ Smartphones und Tablets für sämtliche Beschäftigten für 779 000 Euro.


Im Mai 2024 erhob das Bundesministerium des Innern (BMI) „KI-fähige Infrastruktur in

der Bundesverwaltung“. Das BMI wollte eine Übersicht über KI-Infrastruktur in der


Bundesverwaltung erhalten und einen Auftrag aus der digitalpolitischen St-Runde um­


setzen. Der Bundesrechnungshof hat die Ergebnisse der Abfrage ausgewertet. Sieben


Datenlabore (41 %) hatten insgesamt 59 Grafikkarten [56] beschafft oder betrieben diese


bereits, um KI zu pilotieren oder einzusetzen. Unter den Datenlaboren, die zur Abfrage


des BMI „Fehlanzeige“ meldeten, war auch ein Datenlabor, welches für eine KI-Platt­


form vier Server mit Grafikkarten beschafft hatte. Das AA sah seine Grafikkarten für


PLAIN vor (vgl. Tz. 2.1.1).

### **3.2 Würdigung**


Die in der BHO festgeschriebenen Prinzipien der Wirtschaftlichkeit und Sparsamkeit


sind Grundpfeiler des Verwaltungshandelns. Diese Prinzipien und innovatives Handeln


schließen sich nicht aus. Sie sind auch bei den Datenlaboren zu berücksichtigen. Bei de­


ren Aktivitäten mit externen Dienstleistern hat der Bundesrechnungshof dennoch


strukturelle Defizite feststellen müssen. Ohne WiBe sind angemessene Erfolgskontrol­


len und somit ein „Lernen aus Fehlern“ bei diesen teils sehr innovativen Aktivitäten er­


schwert. Die Bundesregierung wird auch den Erfolg der Datenstrategie nur schwerlich


kontrollieren können, wenn ihr die dazu nötigen Erkenntnisse aus den Aktivitäten der


Datenlabore fehlen.


Der Bundesrechnungshof hat anerkannt, dass sich ein Teil der Datenlabore seit dem


Jahr 2023 darum bemüht hat, Beschaffungen gebündelt durchzuführen. Warum bei


diesem Prozess allerdings bisher nicht alle Datenlabore mitgearbeitet haben, bleibt


………………………………………………………………………………………………………………………………………………………………………………………………………

55 Anlässlich der 13. Sitzung der IMAG Datenlabore.

56 Inklusive Server; ohne Sicherheitsbehörden und Universität der Bundeswehr München im Geschäftsbereich des Bun­

desministeriums der Verteidigung.


#### **27**


offen. Die Datenlabore hätten sich bereits im Jahr 2021 zu Beschaffungen austauschen


und diese bündeln sollen.


Wenn einzelne Datenlabore – insbesondere vor der Entscheidung zu PLAIN – nichts be­


schafft haben, ist fraglich, wie sie dann dazu beitragen wollen, die Ziele der Bundesre­


gierung aus der Datenstrategie zu erreichen. Datenlabore benötigen andere Hard- und


Software als diejenige eines klassischen „Büroarbeitsplatzes“. Diese nicht zu beschaf­


fen, hat die Arbeitsfähigkeit der jeweiligen Datenlabore gefährdet. Es stellt auch die


Wirtschaftlichkeit des Personaleinsatzes in diesen Datenlaboren in Frage. Der Bundes­


rechnungshof hält ferner einzelne Beschaffungen der Datenlabore für nicht wirtschaft­


lich, z. B. die Smartphones und Tablets. [57]


Da die Datenlabore ihre Grafikkarten dem BMI teils nicht gemeldet haben, haben die­


ses und das nunmehr zuständige BMDS kein umfassendes Bild über die KI-Infrastruk­


tur der Bundesverwaltung erhalten können.

### **3.3 Empfehlung**


Der Bundesrechnungshof hat erwartet, dass die Datenlabore künftig die Wirtschaftlich­


keit ihrer Aktivitäten angemessen untersuchen. Dabei sind auch begleitende und ab­


schließende Erfolgskontrollen anhand überprüfbarer, mit messbaren Indikatoren un­


terlegter Ziele vorzusehen. Die Datenlabore sollten sich zu den Indikatoren der WiBe


und den Ergebnissen ihrer Erfolgskontrollen austauschen. Dies wäre z. B. über das


„Peer-to-Peer“-Netzwerk möglich (vgl. Tz. 1.4).


Die Datenlabore sollten ihren Prozess zur „Beschaffungsbündelung“ vorantreiben und


gemeinsam mit dem BeschA bedarfsgerecht Ausschreibungen durchführen. An diesem


Prozess sollten sich alle Datenlabore beteiligen. „Planbarer“ Bedarf ist frühzeitig der


Zentralstelle für IT-Beschaffungen im BeschA zu melden. Die Datenlabore sollten künf­


tig bei jeder Investition in die eigenen DA-Umgebungen prüfen, inwieweit diese mit


Blick auf PLAIN noch erforderlich und wirtschaftlich wäre. Kann PLAIN spezielle Bedarfe


auch absehbar nicht decken, so sollten die Datenlabore weiterhin Beschaffungen


durchführen, um arbeitsfähig zu bleiben.


Die Datenlabore sollten prüfen, inwieweit sie dem BMI tatsächlich korrekte Zahlen zu


den beschafften Grafikkarten zurückgemeldet haben. Falls die gemeldeten Zahlen von


dem tatsächlichen Bestand an Grafikkarten abweichen, sollte das jeweilige Datenlabor


dies dem BMI und dem BMDS nachträglich melden.


………………………………………………………………………………………………………………………………………………………………………………………………………

57 Er hat diese und weitere Prüfungsfeststellungen in gesonderten Prüfungsmitteilungen an die obersten Bundesbe­

hörden der betroffenen Datenlabore festgehalten.


#### **28**


### **3.4 Stellungnahme**

Das BMDS hat auf „Bemühungen der Bundesregierung und des BMDS“ verwiesen, Effi­


zienzpotenziale bei der Staatsmodernisierung und dem Bürokratierückbau auszu­


schöpfen. WiBe seien für wirtschaftliches und sparsames Verwaltungshandeln notwen­


dig. Zu Erfolgskontrollen habe sich das „Peer-to-Peer“-Netzwerk bereits ausgetauscht.


Das BMDS beabsichtige, langfristig planbare Beschaffungen der Datenlabore zu bün­


deln. Aufgrund der Rolle der Datenlabore als „Innovations- und Experimentierräume in


einem höchst komplexen und schnelllebigen Umfeld“ seien aber auch „zügige“ Be­


schaffungen unerlässlich.

### **3.5 Abschließende Würdigung**


Der Bundesrechnungshof erkennt an, dass sich die Datenlabore mittlerweile zu Erfolgs­


kontrollen austauschen. Er erwartet, dass sie künftig die Vorgaben der BHO einhalten.


Dies ist erst recht in politischen Handlungsfeldern des BMDS erforderlich. Gerade die


Rolle der Datenlabore als Innovations- und Experimentierräume machen begleitende


und abschließende Kontrollen der Zielerreichung, Wirkung und Wirtschaftlichkeit ihrer


Aktivitäten für alle anderen Datenlabore besonders wertvoll.


Das BMDS will die Empfehlung des Bundesrechnungshofes zu Beschaffungen teilweise


umsetzen. Es sollte dabei die Bedarfe aller Datenlabore berücksichtigen.


Zur Empfehlung, KI-fähige Infrastruktur der Datenlabore auch vollständig an das BMDS


zu melden, hat dieses sich nicht geäußert. Der Bundesrechnungshof hält an dieser


Empfehlung fest.


#### **29**


## **4 Datenschutz**

### **4.1 Sachverhalt**

Gemäß Artikel 4 Nummer 1 der Datenschutz-Grundverordnung (DSGVO) sind perso­


nenbezogene Daten (pbD) alle Informationen, die sich auf eine identifizierte oder iden­


tifizierbare natürliche Person beziehen. [58]


Artikel 22 DSGVO schützt natürliche Personen vor ausschließlich auf automatisierter


Datenverarbeitung beruhenden Entscheidungen. Artikel 35 DSGVO regelt u. a., in wel­


chen Fällen eine Datenschutz-Folgenabschätzung (DSFA) [59] zu erstellen ist. Dies ist z. B.


dann erforderlich, wenn Einrichtungen große Mengen an pbD automatisiert oder mit­


tels neuer Technologien verarbeiten. [60] Unter den Begriff der „neuen Technologien“ fal­


len dabei auch DA/KI-Verfahren. Alle Datenlabore erprobten oder nutzten solche Ver­


fahren.


Wenn Einrichtungen ihre pbD zunächst geeignet anonymisieren [61], ist die anschlie­


ßende Verarbeitung datenschutzrechtlich unbedenklich [62] . Auch eine pseudonymi­


sierte [63] Verarbeitung kann dazu beitragen, ein angemessenes Schutzniveau der pbD


sicherzustellen. [64]


Im Jahr 2023 empfahl [65] der Bundesrechnungshof den Datenlaboren zu prüfen, inwie­


weit deren Einsatz von DA/KI vollumfänglich DSGVO-konform erfolgt. Eventuell festge­


stellte Mängel sollten die Datenlabore zeitnah abstellen. Er empfahl ferner,


→ in geeigneten Fällen DSFA durchzuführen und


→ pbD künftig anonymisiert oder pseudonymisiert zu verarbeiten.


………………………………………………………………………………………………………………………………………………………………………………………………………

58 Artikel 4 Nummer 1 DSGVO. Als identifizierbar wird eine natürliche Person angesehen, die direkt oder indirekt, insbe­

sondere mittels Zuordnung zu einer Kennung wie einem Namen, zu einer Kennnummer, zu Standortdaten, zu einer
Online-Kennung oder zu einem oder mehreren besonderen Merkmalen, die Ausdruck der physischen, physiologi­
schen, genetischen, psychischen, wirtschaftlichen, kulturellen oder sozialen Identität dieser natürlichen Person sind,
identifiziert werden kann.

59 Eine DSFA beschreibt die geplanten Verarbeitungsvorgänge und deren Zwecke, bewertet deren Notwendigkeit und

Verhältnismäßigkeit sowie die Risiken für die Rechte und Freiheiten der betroffenen Personen und erläutert die ge­
planten Abhilfemaßnahmen, um die Risiken zu bewältigen.

60 Artikel 35 DSGVO, Erwägungsgrund 91 DSGVO (Erforderlichkeit einer DSFA).

61 Um pbD zu anonymisieren, sind diese so zu verändern, dass sie nicht mehr oder nur mit unverhältnismäßigem Auf­

wand einer bestimmten oder bestimmbaren natürlichen Person zugeordnet werden können.

62 Erwägungsgrund 26 DSGVO (keine Anwendung der DSGVO auf anonymisierte Daten).

63 Um pbD zu pseudonymisieren, wird der Name oder ein anderes Identifikationsmerkmal durch ein Pseudonym er­

setzt. Dies soll ausschließen oder wesentlich erschweren, die Identität der natürlichen Person festzustellen. Falls der
dazugehörige Schlüssel bekannt ist, können pseudonymisierte pbD wieder natürlichen Personen zugeordnet wer­
den.


64 Artikel 32 Absatz 1 DSGVO.

65 [Gz.: VII 3 - 0000644 „Datenmanagement in der Bundesverwaltung“ und Gz.: VII 3 - 0000885 „Verfahren der Daten­](https://www.bundesrechnungshof.de/SharedDocs/Downloads/DE/Berichte/2022/datenmanagement-volltext.pdf?__blob=publicationFile&v=4)

[analyse und der künstlichen Intelligenz in der Bundesverwaltung“, Berichte des Bundesrechnungshofes nach](https://www.bundesrechnungshof.de/SharedDocs/Downloads/DE/Berichte/2023/ki-da-volltext.pdf?__blob=publicationFile&v=5)
§ 88 Absatz 2 BHO an den damaligen Beauftragten der Bundesregierung für Informationstechnik.

#### **30**


Die Datenlabore hatten zugesagt, dies zu prüfen und eventuelle Mängel abzustellen.


Im Jahr 2024 gaben daher alle Datenlabore an, dass sie ihre Daten nunmehr DSGVO

konform verarbeiten.


Fünf Datenlabore verarbeiteten pbD. Drei davon verarbeiteten pbD, ohne diese zu


pseudonymisieren oder zu anonymisieren (60 %). Eines [66] dieser Datenlabore führte


eine DSFA durch. [67]

### **4.2 Würdigung**


Der Bundesrechnungshof hat trotz seiner Empfehlungen aus dem Jahr 2023 und der


nachfolgenden Zusagen erneut Mängel beim Datenschutz der Datenlabore festgestellt.


Die Mehrheit der Datenlabore, die pbD verarbeiteten, hat versäumt, diese zu anonymi­


sieren oder zu pseudonymisieren. Diese Datenlabore haben darüber hinaus meist ver­


säumt, eine DSFA zu erstellen. Nur mit einer DFSA hätten sie den notwendigen Schutz­


bedarf angemessen bewerten können. Führen Datenlabore keine DSFA durch, besteht


die Gefahr, dass sie den Schutzbedarf zu niedrig einschätzen und dadurch die Sicher­


heit der Daten nicht gewährleistet ist. Der Bundesrechnungshof sieht hier die Gefahr,


dass einige Datenlabore Betroffenenrechte verletzen.

### **4.3 Empfehlung**


Die Datenlabore sollten erneut prüfen, inwieweit sie ihre Daten derzeit vollumfänglich


DSGVO-konform verarbeiten. Dabei sind die jeweiligen Datenschutzbeauftragten einzu­


binden. Eventuell festgestellte Mängel sind zeitnah abzustellen. Verarbeiten Datenla­


bore mit DA/KI in großen Mengen pbD, so müssen sie eine DSFA durchführen. Ebenso


könnte es z. B. erforderlich sein, pbD künftig anonymisiert oder pseudonymisiert zu


verarbeiten.

### **4.4 Stellungnahme**


Das BMDS hat hervorgehoben, dass der Datenschutz zentral für staatliches Handeln


sei. Es werde einen Austausch bewährter Praktiken im „Peer-to-Peer“ Netzwerk einlei­


ten.


………………………………………………………………………………………………………………………………………………………………………………………………………


66 Bundesministerium für Verkehr.

67 Insgesamt gaben zwei Datenlabore an, eine DSFA durchgeführt zu haben.


#### **31**


### **4.5 Abschließende Würdigung**

Den fachlichen Austausch der Datenlabore, den das BMDS einleiten will, bewertet der


Bundesrechnungshof positiv; er kommt aber angesichts der datenschutzrechtlichen


Kritikalität des Umgangs mit pbD viel zu spät. Auch bleibt unklar, wie die betreffenden


Datenlabore sicherstellen wollen, ihre Daten künftig vollumfänglich DSGVO-konform zu


verarbeiten. Der Bundesrechnungshof bekräftigt seine Empfehlungen. Verstoßen Da­


tenlabore gegen die DSGVO, könnte dies u. a.


→ das Recht auf informationelle Selbstbestimmung verletzen und


→ zu einer negativen Außenwirkung der Bundesverwaltung führen.

## **5 Informationssicherheit und Geheimschutz**

### **5.1 Sachverhalt**

###### **5.1.1 Informationssicherheitskonzepte**


Der UP Bund legt als verbindliche Informationssicherheitsleitlinie des Bundes u. a. fest,


wie Bundesbehörden ihre Informationen und IT-Systeme absichern müssen. [68] ISK die­


nen demnach z. B. dazu,


→ die verarbeiteten Informationen,


→ die durchgeführte Schutzbedarfsfeststellung [69] und


→ die erforderlichen technischen und organisatorischen Schutzmaßnahmen [70]


zu dokumentieren.


71 % der Datenlabore hatten für ihre eigene DA-Umgebung weder das ISK ihrer obers­


ten Bundesbehörde angepasst noch ein eigenes ISK erstellt.


………………………………………………………………………………………………………………………………………………………………………………………………………

68 UP Bund, Leitlinie für die Informationssicherheit in der Bundesverwaltung, S. 3.

69 Ebenda, S. 10.

70 Ebenda.


#### **32**


###### **5.1.2 Geheimschutz**

Verarbeitet eine Behörde mit ihrer IT auch VS, ist die VSA zu beachten. Um sogenannte


„VS-IT“ einsetzen zu dürfen [71], muss ein ISK nach den Standards des IT-Grundschutz­


kompendiums des BSI inklusive der im Geheimschutzbaustein aufgeführten Anforde­


rungen vorliegen. [72] Als Teil der Geheimschutzdokumentation ist die VS-IT zu dokumen­


tieren. [73]


Alle Datenlabore stellten dar, dass sie ihre Daten konform zur VSA verarbeiteten.


Fünf Datenlabore verarbeiteten nach VSA als „VS-NfD“ eingestufte Daten. Zwei davon


hatten weder ein eigenes ISK erstellt noch das ISK ihrer obersten Bundesbehörde über­


arbeitet.

###### **5.1.3 Nutzung externer Cloud-Dienste**


Gemäß IT-Grundschutz-Kompendium und dem Mindeststandard des BSI für externe


Cloud-Dienste [74] müssen Behörden eine Strategie für die Cloud-Nutzung erstellen. [75]


Diese muss Ziele, Chancen und Risiken der Cloud-Nutzung enthalten. Die Behörde


muss zudem rechtliche und organisatorische Rahmenbedingungen sowie technische


Anforderungen untersuchen und in einer Machbarkeitsstudie dokumentieren. Darauf


aufbauend ist eine Sicherheitsrichtlinie für die Cloud-Nutzung sowie ein Sicherheitskon­


zept für den Cloud-Dienst zu erstellen. [76]


82 % der Datenlabore nutzten externe Cloud-Dienste. Die Hälfte dieser Datenlabore ga­


ben an, sie hielten mit ihrer Cloud-Nutzung den Mindeststandard des BSI ein.


Der Bundesrechnungshof stellte fest, dass 18 % aller Datenlabore eine Cloud-Strategie


erstellt hatten (vgl. Abbildung 3). Ebenfalls 18 % hatten eine Sicherheitsrichtlinie für die


Cloud-Nutzung oder ein Sicherheitskonzept für den Cloud-Dienst erstellt. Ein Datenla­


bor hatte alle Dokumente erstellt, die der Mindeststandard des BSI fordert. [77]


………………………………………………………………………………………………………………………………………………………………………………………………………

71 „Die Verarbeitung von [VS] ist nur mit VS-IT zulässig, die hierfür freigegeben ist.“, § 50 VSA.

72 IT-Grundschutzkompendium des BSI, CON.11.1 (Geheimschutz VS-NUR FÜR DEN DIENSTGEBRAUCH).

73 IT-Grundschutzkompendium des BSI, CON.11.1.A2 (Erstellung und Fortschreibung der VS-IT-Dokumentation nach

§ 12 und Nummer 2.2 Anlage II zur VSA).

74 „Mindeststandard des BSI zur Nutzung externer Cloud-Dienste nach § 8 Absatz 1 Satz 1 BSIG“ – Version 2.1 vom

15. Dezember 2022.

75 IT-Grundschutz-Kompendium des BSI, OPS.2.2.A1 (Erstellung einer Strategie für die Cloud-Nutzung).

76 IT-Grundschutz-Kompendium des BSI, OPS.2.2.A2 (Erstellung einer Sicherheitsrichtlinie für die Cloud-Nutzung) und

OPS.2.2.A7 (Erstellung eines Sicherheitskonzeptes für die Cloud-Nutzung).

77 AA.


#### **33**


Abbildung 3

#### **Mindeststandard für externe Cloud-Dienste mehrheitlich nicht** **erfüllt**


Die überwiegende Mehrheit der Datenlabore erfüllte den Mindeststandard nicht, da einzelne


oder alle der darin geforderten Dokumente fehlten.

















Grafik: Bundesrechnungshof. Quelle: Auswertung von Erhebungsdaten.

### **5.2 Würdigung**


Die Mehrheit der Datenlabore hat gegen den UP Bund verstoßen, da sie entweder kein


eigenes ISK erstellt haben oder die jeweilige oberste Bundesbehörde ihr ISK nicht ge­


eignet fortgeschrieben hat. Es ist nicht nachvollziehbar, wieso dieser Mangel noch


Jahre später auftritt – einige Datenlabore bestehen bereits seit dem Jahr 2021. Zwei Da­


tenlabore haben darüber hinaus die Vorgaben der VSA nicht eingehalten, da sie VS-IT


ohne gültiges ISK nutzten.


Obwohl die Hälfte der Datenlabore, die verwaltungsexterne Cloud-Dienste nutzten, da­


von ausgingen, den Mindeststandard des BSI zur Nutzung externer Cloud-Dienste zu


erfüllen, hielt diesen nur ein Datenlabor ein. Die anderen Datenlabore hatten wesentli­


che Teile oder alle der im Mindeststandard vorgesehenen Dokumente nicht erstellt.

### **5.3 Empfehlung**


Die Datenlabore haben die Vorgaben des UP Bund, der VSA und des IT-Grundschutz­


kompendiums einzuhalten. Dafür noch fehlende ISK sind zeitnah zu erstellen oder das


jeweilige ISK der obersten Bundesbehörde fortzuschreiben. Dies gilt umso mehr, wenn


Datenlabore VS verarbeiten.


Nutzen Datenlabore verwaltungsexterne Cloud-Dienste, müssen sie den Mindeststan­


dard des BSI zur Nutzung externer Cloud-Dienste einhalten. Dazu noch fehlende


#### **34**


Dokumente sollten sie zeitnah erstellen und sich dabei eng mit ihren jeweiligen Infor­


mationssicherheitsbeauftragten abstimmen.

### **5.4 Stellungnahme**


Das BMDS hat hervorgehoben, dass die Informationssicherheit zentral für staatliches


Handeln sei. Es werde dazu einen Austausch im „Peer-to-Peer“ Netzwerk einleiten.

### **5.5 Abschließende Würdigung**


Das BMDS lässt offen, wie die Datenlabore planen, künftig die Vorgaben


→ des UP Bund [78],


→ der VSA,


→ des IT-Grundschutzkompendiums und


→ des Mindeststandards des BSI zur Nutzung externer Cloud-Dienste


einzuhalten. Sich dazu im „Peer-to-Peer“-Netzwerk auszutauschen, ist grundsätzlich


sinnvoll. Es entbindet jedes einzelne Datenlabor aber nicht davon, fehlende ISK kurz­


fristig zu erarbeiten oder anzupassen und die weiteren Empfehlungen umzusetzen.


Der Bundesrechnungshof hält an diesen fest.

## **6 IT-Betrieb**

### **6.1 Sachverhalt**


Die Datenlabore entwickelten ihre „Datenprodukte“ teils bis zur Betriebsreife. Dabei


stellten sich regelmäßig Fragen, wie die Datenlabore in übliche Prozesse der jeweiligen


IT-Betriebsorganisation einzubinden wären, u. a.


→ welche Organisationseinheit den Betrieb „fertiger“ Datenprodukte verantwortet,


→ inwieweit Datenlabore ihre Datenprodukte an andere Organisationseinheiten oder


Behörden übergeben können,


→ welche „Verfügbarkeit“ Beschäftigte von Datenprodukten erwarten und


………………………………………………………………………………………………………………………………………………………………………………………………………


78 Seit Dezember 2025 ist hier zusätzlich § 44 Absatz 1 des Gesetzes über das BSI und über die Sicherheit in der Infor­


mationstechnik von Einrichtungen zu beachten.


#### **35**


→ inwieweit dies von Betriebsverantwortlichen – also z. B. dem jeweiligen IT-Referat


oder IT-Dienstleister [79] – leistbar ist.


In diesem Zusammenhang nannten die Datenlabore dem Bundesrechnungshof als


Probleme u. a. „Betrieb und Support“, „Betrieb von Protoypen“ und „unklare Zuständig­


keiten“.


Beispiel 1 – Übergabe von Datenprodukten an das IT-Referat


Ein Datenlabor entwickelte für seine oberste Bundesbehörde ein Datenprodukt „Fact


Sheet“. Dieses stellte für verschiedene Organisationseinheiten der obersten Bundesbe­


hörde relevante Kennzahlen und Statistiken dar.


Die fachlich und betrieblich zuständigen Abteilungsleitungen [80] einigten sich darauf,


dass das IT-Referat den Betrieb des Datenproduktes vom Datenlabor übernehmen

sollte. Die fachliche Übergabe des Anwendungsfalls erfolgte im Juni 2024. Im Novem­

ber 2024 stand die technische Übergabe an das IT-Referat noch aus.


Bei einem weiteren Datenprodukt des Datenlabors stand die technische Übergabe an


das IT-Referat seit über einem Jahr aus. In seinem Risikomanagement führte das Da­


tenlabor demnach das Risiko „Kapazitätsbindung wg. verzögerter [Datenprodukt]
Übergabe“.































………………………………………………………………………………………………………………………………………………………………………………………………………

79 Bei sogenannte „vollkonsolidierten“ Datenlaboren.

80 Zentralabteilung und Leitungsabteilung.


#### **36**


### **6.2 Würdigung**

Die Beispiele legen nahe, dass die Datenlabore noch grundlegende Fragen ihrer Zu­


sammenarbeit mit der jeweiligen IT-Betriebsorganisation klären müssen. Sie haben


versäumt, diejenigen Datenprodukte, die Beschäftigte auch über längere Zeit nutzen


sollen, geeignet an Betriebsverantwortliche außerhalb der Datenlabore zu übergeben.


Es ist nicht angemessen, dass


→ Behörden, für die ein Datenprodukt entwickelt wurde, sich anschließend weigern,


dieses zu übernehmen,


→ fehlende Übergaben den langfristigen Betrieb als „erfolgreich“ eingeschätzter Da­


tenprodukte gefährden und


→ Beschäftigte der Datenlabore selbst Betriebsverantwortung für Datenprodukte über­


nehmen müssen,


       - was ihre Kapazitäten für innovatives Verwaltungshandeln einschränkt und


       - zu einem „best effort“ Betrieb führt, den der Bundesrechnungshof nicht bei jedem


Datenprodukt für angemessen hält.


„Best effort“ könnte hier u. a. bedeuten, dass


→ Datenlabore keine angemessene Verfügbarkeit für Datenprodukte garantieren kön­


nen,


→ Fehler oder Sicherheitslücken bei Datenprodukten unbemerkt bleiben oder nicht


zeitgerecht behoben werden und


→ Fragen von Nutzenden zu Datenprodukten über längere Zeit unbeantwortet bleiben.


………………………………………………………………………………………………………………………………………………………………………………………………………

81 „Best effort“ ist eine minimalistische Dienstgüte-Zusicherung. Es bedeutet, dass die Betriebsverantwortlichen Anfra­

gen innerhalb ihrer üblichen Verfügbarkeiten bearbeiten. Das ITZBund bietet z. B. mit „best effort“ Kunden seine
niedrigste Serviceklasse-/zeiten-Kombination ohne Zielwerte für laufende Betriebsleistungen an.


#### **37**


### **6.3 Empfehlung**

Die Datenlabore sollten darauf hinwirken, dass sie alle Datenprodukte, die Beschäftigte


über längere Zeit nutzen sollen, an ihre jeweils zuständige IT-Betriebsorganisation


übergeben. Die Datenlabore könnten zunächst ihre Erfahrungen mit (ggf. gescheiter­


ten) Betriebsübergaben für Datenprodukte untereinander austauschen. Dazu könnten


sie z. B. das „Peer-to-Peer“-Netzwerk nutzen. Sie sollten anschließend gemeinsam


einen Prozess erarbeiten, wie eine geordnete Betriebsübergabe eines Datenproduktes


aussehen könnte. Den Prozess sollten sie anschließend in enger Abstimmung mit den


Betriebsverantwortlichen ihrer jeweiligen obersten Bundesbehörden umsetzen. Zu be­


teiligende Gremien und Beauftragte, z. B. Personalvertretungen oder Datenschutzbe­


auftragte, haben die Datenlabore dabei geeignet einzubinden.


Für eine Betriebsübergabe eines Datenproduktes wäre aus Sicht des Bundesrech­


nungshofes u. a. Folgendes erforderlich und schriftlich festzuhalten:


→ Schutzbedarfsfeststellung und ISK,


→ Anforderungen an den Betrieb, z. B. zu erforderlichen Serviceklassen und -zeiten,


→ Betriebshandbuch,


→ Handlungsanweisung für den Helpdesk oder Servicedesk,


→ falls erforderlich ein Rechte-/Rollenkonzept,


→ Nutzendenhandbuch/-Dokumentation und


→ datenschutzrechtliche Dokumentation.

### **6.4 Stellungnahme**


Das BMDS hat die Auffassung vertreten, dass bei entsprechender Reife und Zielsetzung


„zu prüfen“ sei, Datenprodukte an geeignete Betriebsverantwortliche zu übergeben.

### **6.5 Abschließende Würdigung**


Bloß zu prüfen, dauerhaft nutzbare Datenprodukte an Betriebsverantwortliche zu


übergeben, wird den erfolgskritischen Entwicklungsaufgaben der Datenlabore nicht

gerecht. Übergabeprozesse für in den Datenlaboren erstellte, betriebsreife Datenpro­


dukte in den obersten Bundesbehörden sind so zu gestalten, dass deren geordneter


Betrieb dauerhaft sichergestellt ist. Der Bundesrechnungshof hält an seinen Empfeh­


lungen fest.


#### **38**


## **7 Fazit**

Behörden und Einrichtungen des Bundes benötigen Freiräume, um mit innovativen


Technologien wie DA/KI zu experimentieren, diese zu erproben und um daraus zu ler­


nen. Die Datenlabore sind dafür grundsätzlich geeignete Organisationseinheiten. Aller­


dings braucht es ein wirtschaftliches, durchdachtes und überprüfbares Vorgehen, um


die strategischen Ziele der Bundesregierung zu erreichen und datenbasiertes Vorge­


hen in der Bundesverwaltung weiter voranzutreiben.


Der Bundesrechnungshof hat zahlreiche strukturelle Mängel bei den Datenlaboren


festgestellt. U. a.


→ waren einige Datenlabore immer noch nicht arbeitsfähig, da grundlegende Infra­


struktur gefehlt hat (vgl. Tz. 2.1),


→ haben die Datenlabore in vielen Fällen darauf verzichtet, eine WiBe zu erstellen und


somit gegen Haushaltsrecht verstoßen (vgl. Tz. 3.1.1),


→ haben die Datenlabore Empfehlungen des Bundesrechnungshofes zum Datenschutz


teils noch nicht umgesetzt (vgl. Tz. 4.1),


→ hat die Mehrheit der Datenlabore gegen Vorgaben des IT-Grundschutzes, der VSA


und den Mindeststandard für externe Cloud-Dienste des BSI verstoßen (vgl. Tz. 5.1)


und


→ müssen die Datenlabore noch grundlegende Fragen der Zusammenarbeit mit den


für den IT-Betrieb ihrer jeweiligen obersten Bundesbehörden zuständigen Stellen


klären (vgl. Tz. 6.1).


Angesichts dieser Mängel hat der Bundesrechnungshof es für dringend erforderlich


gehalten, dass die obersten Bundesbehörden in ihrer jeweiligen Zuständigkeit stärker


darauf hinarbeiten, beim weiteren Auf- und Ausbau ihrer Datenlabore


→ die strategischen Ziele der Bundesregierung zu erreichen und


→ dabei wirtschaftlich und ordnungsgemäß vorzugehen.


Der Bundesrechnungshof hat erwartet, dass die Datenlabore dazu seine Empfehlun­


gen berücksichtigen. Das nunmehr zuständige BMDS sollte diesen Prozess eng beglei­


ten und koordinieren. Es könnte dazu einen „Leitfaden für Datenlabore oberster Bun­


desbehörden“ erstellen und von der IMAG Datenlabore beschließen lassen. Der


Leitfaden sollte insbesondere regeln, wie die Empfehlungen des Bundesrechnungsho­


fes durch die Datenlabore umzusetzen sind.


#### **39**


### **7.1 Stellungnahme**

Das BMDS hat dargestellt, zentrales Leitmotiv für die Datenlabore sei es, wirkungsvol­


les staatliches Handeln durch evidenzbasierte Entscheidungsfindung zu stärken. Die


Datenlabore der Bundesregierung arbeiteten eng zusammen und hätten bereits zahl­


reiche nachweisbare Mehrwerte generiert. Fachliche Bedarfe, besondere Eigenheiten,


strategische und konzeptionelle Fragen der obersten Bundesbehörden seien dabei zu


berücksichtigen. Diese beeinflussten die Umsetzbarkeit und Wirksamkeit der Empfeh­


lungen des Bundesrechnungshofes. Daher seien gemeinsame Standards, Prozesse und


Strukturen nur dort anzustreben, „wo die Rahmenbedingungen dies zulassen“. Die Da­


tenlabore hätten aus den Empfehlungen des Bundesrechnungshofes „konkrete Maß­


nahmen“ abgeleitet.

### **7.2 Abschließende Würdigung**


Der Bundesrechnungshof erkennt an, dass die Datenlabore das staatliche Handeln


durch evidenzbasierte Entscheidungen stärken wollen. Um dieses zentrale Ziel zu errei­


chen, sollten die obersten Bundesbehörden seine Empfehlungen beachten und nicht


implizit auf das Ressortprinzip [82] verweisen. „Konkrete Maßnahmen“ kann der Bundes­


rechnungshof in der Stellungnahme des BMDS kaum ausmachen. Dabei besteht im Be­


reich des datenbasierten Verwaltungshandelns seit Jahren [83] dringender Handlungsbe­


darf, dem die Bundesregierung aktuell mit ihrer Modernisierungsagenda begegnen


will: Damit der „Einsatz von KI auf einer soliden Datenbasis erfolgen kann“ [84], ist „die


notwendige Grundlagenarbeit an den Datenbeständen zu priorisieren“ [85] (vgl. Tz. 1.3).


Für den Bundesrechnungshof bleibt offen, wie die Bundesregierung dies ohne


→ geeignet ausgestattete sowie


→ datenschutzkonform, sicher und wirtschaftlich arbeitende


Datenlabore umsetzen will. Die Datenlabore sollten der Bundesverwaltung als Vorbild


vorangehen und über ihre wegweisende Zusammenarbeit unter gemeinsamen Stan­


dards, Prozessen und Strukturen aufzeigen, wie zeitgemäßes Verwaltungshandeln aus­


sehen könnte.


………………………………………………………………………………………………………………………………………………………………………………………………………

82 Artikel 65 Satz 2 Grundgesetz.

83 [Gz.: VII 3 - 0000644 „Datenmanagement in der Bundesverwaltung“ und Gz.: VII 3 - 0000885 „Verfahren der Daten­](https://www.bundesrechnungshof.de/SharedDocs/Downloads/DE/Berichte/2022/datenmanagement-volltext.pdf?__blob=publicationFile&v=4)

[analyse und der künstlichen Intelligenz in der Bundesverwaltung“, Berichte des Bundesrechnungshofes nach](https://www.bundesrechnungshof.de/SharedDocs/Downloads/DE/Berichte/2023/ki-da-volltext.pdf?__blob=publicationFile&v=5)
§ 88 Absatz 2 BHO an den damaligen Beauftragten der Bundesregierung für Informationstechnik.

84 Modernisierungsagenda, S. 36.

85 Ebenda.

#### **40**


Der Bundesrechnungshof empfiehlt daher weiterhin, einen „Leitfaden für Datenlabore


oberster Bundesbehörden“ zu erstellen und von der IMAG Datenlabore beschließen zu


lassen. Er beabsichtigt, den weiteren Aufbau und die vorgesehene Verstetigung der Da­


tenlabore in den kommenden Jahren eng zu begleiten.


Essers Cäsar


Beglaubigt: Petra Schmid, Tarifbeschäftigte
Wegen elektronischer Bearbeitung ohne Unterschrift und Dienstsiegelabdruck.


#### **41**


