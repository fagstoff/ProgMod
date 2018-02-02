# Retningslinjer for bidrag

Ønsker du å bidra med innholdsproduksjon kan det enkelt gjøres ved å:

1. Lag en [fork](https://github.com/fagstoff/ProgMod#fork-destination-box) av dette repoet.
1. Gjør endringer/lag innhold.
1. Legg inn en [pull request](https://help.github.com/articles/about-pull-requests/) her.
1. Følg retningslinjene som er beskrevet under

>TODO: Lage videotutorial?

> TODO: Generell intro om hvorfor vi har retningslinjer...

Retningslinjene er delt inn i tre hovedområder:

 * [Standard for utforming av fagstoff-sider](#standard-for-utforming-av-fagstoff-sider)
 * [Programkode](#programkode)
 * [Prosjektoppgaver](#prosjektoppgaver)
 
 
## Standard for utforming av fagstoff-sider

Alle fagstoffsider skal oppfylle kravene som er gitt nedenfor.

### Generelle krav

 * Alle fagstoffsider skal implementeres som [Jupyter notebooks](https://jupyter.org/install.html)
 * Alle fagstoffsideer skal merkes med en [Creative Commons-lisens](https://creativecommons.org/choose/?lang=no)
    * Foretrukket lisens er [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.no)

### Krav til innhold

Første celle i notebook-en skal ha følgende innhold:

 * Tittel på notebook-en
 * Linjen etter tittelen skal inneholde lisensinformasjon og navn på opphavsmenn
 * Fagteksten skal starte med en kort ingress som gir en introduksjon til fagstoffet som skal behandles.
 * Sammen med ingressen bør det være et illustrerende bilde eller figur. Bildet skal være ca. 200 piksler i bredden, og skal flyte til høyre for ingressen.
 * Etter ingressen skal det stå opplysninger om relevante læreplanmål

Andre celle i notebook-en skal ha følgende innhold:
 * Fagtekst
 * Matematikk som er typesatt med LaTeX (der hvor det er aktuelt)
 * En eller flere figurer som illustrerer fagteksten

Tredje celle i notebook-en skal ha følgende innhold:
 * Python-kode
 * Koden bør ligge så nært opp til standarden [PEP-8](https://www.python.org/dev/peps/pep-0008/) som mulig

Standarden for tredje og fjerde celle gjentas så mange ganger som nødvendig gjennom resten av notebook-en (veksler mellom fagtekst og programkode).

Nest siste celle i notebook-en skal ha følgende innhold:
 * En oppsummering av fagstoffet som er behandlet

Siste celle i notebook-en skal ha følgende innhold:
 * Oppgaver
 * Større (tidkrevende) oppgaver skal implementeres som egne "Prosjektoppgaver"


# Programkode

> TODO

# Prosjektoppgaver

> TODO
 
