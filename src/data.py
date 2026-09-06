PROGETTI = {
    "it": [
        {
            "titolo": "KonaKart",
            "descrizione": "Piattaforma di e-commerce basata su Java pensata per la gestione di negozi online di medie e grandi dimensioni",
        },
        {
            "titolo": "Reporting Studio",
            "descrizione": "Sistema di reportistica avanzata e personalizzazione grafica integrato all'interno dell'ecosistema di software gestionali Mago",
        },
        {
            "titolo": "LR Documentation Exporter",
            "descrizione": "Tool per esportare documentazione da un portale Liferay",
        }
    ],
    "en": [
        {
            "titolo": "KonaKart",
            "descrizione": "E-commerce platform based on Java designed for managing online stores of medium and large size",
        },
        {
            "titolo": "Reporting Studio",
            "descrizione": "Advanced reporting system with graphical customization integrated within the Mago management software ecosystem",
        },
        {
            "titolo": "LR Documentation Exporter",
            "descrizione": "Tool for exporting documentation from a Liferay portal",
        }
    ]
}

COMPETENZE = {
    "it": [
        "Java 8", "C#", "Typescript", "Angular", "Javascript", "React", "CSS", "SQL", "Docker", "Podman", "HTML",
        "Git", "C++", "Maven", "Ant", "SVN", "Apache Tomcat", "Eclipse", "IntelliJ IDEA", "Visual Studio Code",
        "Spring Boot 2", "Visual Studio", "DBeaver", "Postman", "JUnit 4", "OpenXML"
    ],
    "en": [
        "Java 8", "C#", "Typescript", "Angular", "Javascript", "React", "CSS", "SQL", "Docker", "Podman", "HTML",
        "Git", "C++", "Maven", "Ant", "SVN", "Apache Tomcat", "Eclipse", "IntelliJ IDEA", "Visual Studio Code",
        "Spring Boot 2", "Visual Studio", "DBeaver", "Postman", "JUnit 4", "OpenXML"
    ]
}

ESPERIENZE = {
    "it": [
        {
            "ruolo": "Full Stack Developer",
            "azienda": "Zucchetti S.p.A.",
            "periodo": "Dicembre 2020 - Presente",
            "descrizione": "Sviluppo di applicazioni web e desktop per la gestione di software gestionali, con focus su Java, C# e tecnologie front-end come Angular.",
        },
        {
            "ruolo": "IT Consultant / Engineer",
            "azienda": "Altran Italia S.p.A.",
            "periodo": "Marzo 2015 - Novembre 2020",
            "descrizione": "Collaborazione nello sviluppo di soluzioni software personalizzate per clienti aziendali, partecipando a tutte le fasi del ciclo di vita del software.",
        },
        {
            "ruolo": "IT Consultant",
            "azienda": "Network Integrations and Solutions S.r.l.",
            "periodo": "Ottobre 2008 - Febbraio 2015",
            "descrizione": "Collaborazione nello sviluppo di soluzioni software personalizzate per clienti aziendali, partecipando a tutte le fasi del ciclo di vita del software.",
        },
        {
            "ruolo": "Java Developer",
            "azienda": "Avelco Italia S.r.l.",
            "periodo": "Gennaio 2008 - Ottobre 2008",
            "descrizione": "Porting di moduli e componenti software da un gestionale legacy ad un applicazione web.",
        },
        {
            "ruolo": "Cobol Junior Developer",
            "azienda": "Omnia Informatica S.r.l.",
            "periodo": "Aprile 2007 - Dicembre 2007",
            "descrizione": "Aggiornamento software gestionale in base ai requisiti del cliente, sviluppo dell'interfaccia utente e generazione di report.",
        }
    ],
    "en": [
        {
            "ruolo": "Full Stack Developer",
            "azienda": "Zucchetti S.p.A.",
            "periodo": "December 2020 - Present",
            "descrizione": "Development of web and desktop applications for management software, with a focus on Java, C#, and front-end technologies such as Angular.",
        },
        {
            "ruolo": "IT Consultant / Engineer",
            "azienda": "Altran Italia S.p.A.",
            "periodo": "March 2015 - November 2020",
            "descrizione": "Collaboration in the development of customized software solutions for corporate clients, participating in all phases of the software development lifecycle.",
        },
        {
            "ruolo": "IT Consultant",
            "azienda": "Network Integrations and Solutions S.r.l.",
            "periodo": "October 2008 - February 2015",
            "descrizione": "Collaboration in the development of customized software solutions for corporate clients, participating in all phases of the software development lifecycle.",
        },
        {
            "ruolo": "Java Developer",
            "azienda": "Avelco Italia S.r.l.",
            "periodo": "January 2008 - October 2008",
            "descrizione": "Porting of software modules and components from a legacy management system to a web application.",
        },
        {
            "ruolo": "Cobol Junior Developer",
            "azienda": "Omnia Informatica S.r.l.",
            "periodo": "April 2007 - December 2007",
            "descrizione": "Updating management software based on client requirements, developing the user interface, and generating reports.",
        }
    ]
}

EMAIL_CONTATTO = "alessandro.casamassima@gmail.com"

def get_progetti(locale):
    return PROGETTI.get(locale, PROGETTI["it"])

def get_competenze(locale):
    return COMPETENZE.get(locale, COMPETENZE["it"])

def get_esperienze(locale):
    return ESPERIENZE.get(locale, ESPERIENZE["it"])