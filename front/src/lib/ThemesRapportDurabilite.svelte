<script>
let environnement = {
    "titre": "ESRS E1 - Changement climatique",
    "etat": false,
    "sousThemes": {
        "adaptation": false,
        "attenuation": false,
        "energie": false
    }
}

function handleClick(theme) {
	console.log(theme)
    environnement.sousThemes[theme] = ! environnement.sousThemes[theme]
    console.log(environnement)
}
</script>

<div class="fr-grid-row fr-grid-row--gutters rse-organizer">
    <div class="fr-col-12">
        <div class="rse-organizer--container rse-organizer--gov">
            <div class="rse-organizer--header">
                <h4 class="rse-organizer--title">Général</h4>
            </div>
            <div class="rse-organizer--content">
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS1">
                        <div class="rse-organizer--card-title">
                            <b>ESRS 1 - Exigences générales</b>
                        </div>
                        <p class="fr-collapse fr-text--sm" id="accordion-ESRS1">
                            L'ESRS 1, à visée informative, instruit les principes généraux de la CSRD, comme sa temporalité et la forme que doit prendre le Rapport de Durabilité.
                        </p>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS 1" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRS1"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <div class="rse-organizer--card rse-organizer--card-disabled" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS2">
                        <div class="rse-organizer--card-title">
                            <b>ESRS 2 - Informations générales à publier</b>
                        </div>
                    </div>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS 2" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRS2"></button>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-col-lg-4 fr-col-12">
        <div class="rse-organizer--container rse-organizer--env">
            <div class="rse-organizer--header">
                <h4 class="rse-organizer--title">Environnement</h4>
            </div>
            <div class="rse-organizer--content">
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-E1">
                        <div class="rse-organizer--card-title">
                            <input name="checkboxes-23" id="checkboxes-23" type="checkbox" aria-describedby="checkboxes-23-messages">
                            <b>{ environnement.titre }</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-text--sm" id="accordion-ESRS-E1">
                                <li><input name="checkboxes4" id="checkboxes4id" type="checkbox" aria-describedby="checkboxes-4-messages" on:click={() =>handleClick("adaptation")}> Adaptation au changement climatique</li>
                                <li><input name="checkboxes5" id="checkboxes5id" type="checkbox" aria-describedby="checkboxes-5-messages" on:click={() =>handleClick("attenuation")}> Atténuation du changement climatique</li>
                                <li><input name="checkboxes6" id="checkboxes6id" type="checkbox" aria-describedby="checkboxes-6-messages" on:click={() =>handleClick("energie")}> Energie</li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS E1" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSE1"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-E2">
                        <div class="rse-organizer--card-title">
                            <b>ESRS E2 - Pollution</b>
                        </div>
                        <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-E2">
                            <li>Pollution de l'air</li>
                            <li>Pollution des eaux</li>
                            <li>Pollution des sols</li>
                            <li>Pollution des organismes vivants et des ressources alimentaires</li>
                            <li>Substances préoccupantes</li>
                            <li>Substances extrêmement préoccupantes</li>
                            <li>Microplastiques</li>
                        </ul>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS E2" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSE2"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-E3">
                        <div class="rse-organizer--card-title">
                            <b>ESRS E3 - Ressources aquatiques et marines</b>
                        </div>
                        <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-E3">
                            <li>Eau</li>
                            <li>Ressources marines</li>
                            <li>
                                <ul>
                                    <li>Consommation d'eau</li>
                                    <li>Prélèvements d'eau</li>
                                    <li>Rejet des eaux</li>
                                    <li>Rejet des eaux dans les océans</li>
                                    <li>Extraction et utilisation des ressources marines</li>
                                </ul>
                            </li>
                        </ul>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS E3" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSE3"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-E4">
                        <div class="rse-organizer--card-title">
                            <b>ESRS E4 - Biodiversité et écosystèmes</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-E4">
                                <li>Vecteurs d'incidence directs de la perte de biodiversité</li>
                                <li>
                                    <ul>
                                        <li>Changement climatique</li>
                                        <li>Changement d'affectation des terres, changement d'utilisation de l'eau douce et des mers</li>
                                        <li>Exploitation directe</li>
                                        <li>Espèces exotiques envahissantes</li>
                                        <li>Pollution</li>
                                        <li>Autres</li>
                                    </ul>
                                </li>
                                <li>Incidence sur l'état des espèces</li>
                                <li>Incidences sur l'étendue et l'état des écosystèmes</li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS E4" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSE4"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-E5">
                        <div class="rse-organizer--card-title">
                            <b>ESRS E5 - Economie circulaire</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-E5">
                                <li>Ressources entrantes, y compris l'utilisation des ressources</li>
                                <li>Ressources sortantes liées aux produits et services</li>
                                <li>Déchets</li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS E5" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSE5"></button>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-col-lg-4 fr-col-12">
        <div class="rse-organizer--container rse-organizer--social">
            <div class="rse-organizer--header">
                <h4 class="rse-organizer--title">Social</h4>
            </div>
            <div class="rse-organizer--content">
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-S1">
                        <div class="rse-organizer--card-title">
                            <b>ESRS S1 - Effectifs de l’entreprise</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-S1">
                                <li>Conditions de travail</li>
                                <li>
                                    <ul>
                                        <li>Sécurité de l'emploi</li>
                                        <li>Temps de travail</li>
                                        <li>Salaires décents</li>
                                        <li>Dialogue social</li>
                                        <li>Liberté d'association, existence de comités d'entreprise et droits des travailleurs à l'information, à la consultation et à la participation</li>
                                        <li>Négociation collective, y compris la proportion de travailleurs couverts par des conventions collectives</li>
                                        <li>Equilibre entre vie professionnelle et vie privée</li>
                                        <li>Santé et sécurité</li>
                                    </ul>
                                </li>
                                <li>Egalité de traitement et égalité des chances pour tous</li>
                                <li>
                                    <ul>
                                        <li>Egalité de genre et égalité de rémunération pour un travail de valeur égale</li>
                                        <li>Formation et développement des compétences</li>
                                        <li>Emploi et inclusion des personnes handicapées</li>
                                        <li>Mesures de lutte contre la violence et le harcèlement sur le lieu de travail</li>
                                        <li>Diversité</li>
                                    </ul>
                                </li>
                                <li>Autres droits liés au travail</li>
                                <li>
                                    <ul>
                                        <li>Travail des enfants</li>
                                        <li>Travail forcé</li>
                                        <li>Logement adéquat</li>
                                        <li>Protection de la vie privée</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS S1" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSS1"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-S2">
                        <div class="rse-organizer--card-title">
                            <b>ESRS S2 - Travailleurs de la chaîne de valeurs</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-S2">
                                <li>Conditions de travail</li>
                                <li>
                                    <ul>
                                        <li>Sécurité de l'emploi</li>
                                        <li>Temps de travail</li>
                                        <li>Salaires décents</li>
                                        <li>Dialogue social</li>
                                        <li>Liberté d'association y compris l'existence de comités d'entreprise</li>
                                        <li>Négociations collective</li>
                                        <li>Equilibre entre vie professionnelle et vie privée</li>
                                        <li>Santé et sécurité</li>
                                    </ul>
                                </li>
                                <li>Egalité de traitement et égalité des chances pour tous</li>
                                <li>
                                    <ul>
                                        <li>Egalité de genre et égalité de rémunération pour un travail de valeur égale</li>
                                        <li>Formation et développement des compétences</li>
                                        <li>Emploi et inclusion des personnes handicapées</li>
                                        <li>Mesures de lutte contre la violence et le harcèlement sur le lieu de travail</li>
                                        <li>Diversité</li>
                                    </ul>
                                </li>
                                <li>Autres droits liés au travail</li>
                                <li>
                                    <ul>
                                        <li>Travail des enfants</li>
                                        <li>Travail forcé</li>
                                        <li>Logement adéquat</li>
                                        <li>Eau et assainissement</li>
                                        <li>Protection de la vie privée</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS S2" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSS2"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-S3">
                        <div class="rse-organizer--card-title">
                            <b>ESRS S3 - Communautés touchées</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-S3">
                                <li>Droits économiques, sociaux et culturels des communautés</li>
                                <li>
                                    <ul>
                                        <li>Logement adéquat</li>
                                        <li>Alimentation adéquate</li>
                                        <li>Eau et assainissement</li>
                                        <li>Incidences liées à la terre</li>
                                        <li>Incidences liées à la sécurité</li>
                                    </ul>
                                </li>
                                <li>Droits civils et politiques des communautés</li>
                                <li>
                                    <ul>
                                        <li>Liberté d’expression</li>
                                        <li>Liberté de réunion</li>
                                        <li>Incidences sur les défenseurs des droits de l’homme</li>
                                    </ul>
                                </li>
                                <li>Droits des peuples autochtones</li>
                                <li>
                                    <ul>
                                        <li>Consentement préalable, donné librement et en connaissance de cause</li>
                                        <li>Auto-détermination</li>
                                        <li>Droits culturels</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS S3" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSS3"></button>
                </div>
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-S4">
                        <div class="rse-organizer--card-title">
                            <b>ESRS S4 - Consommateurs et utilisateurs finals</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-S4">
                                <li>Incidences liées aux informations sur les consommateurs et/ou les utilisateurs finals</li>
                                <li>
                                    <ul>
                                        <li>Protection de la vie privée</li>
                                        <li>Liberté d’expression</li>
                                        <li>Accès à l’information (de qualité)</li>
                                    </ul>
                                </li>
                                <li>Sécurité des consommateurs et/ou des utilisateurs finals</li>
                                <li>
                                    <ul>
                                        <li>Santé et sécurité</li>
                                        <li>Sécurité de la personne</li>
                                        <li>Protection des enfants</li>
                                    </ul>
                                </li>
                                <li>Inclusion sociale des consommateurs et/ou des utilisateurs finals</li>
                                <li>
                                    <ul>
                                        <li>Non-discrimination</li>
                                        <li>Accès aux produits et services</li>
                                        <li>Pratiques de commercialisation responsables</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS S4" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSS4"></button>
                </div>
            </div>
        </div>
    </div>
    <div class="fr-col-lg-4 fr-col-12">
        <div class="rse-organizer--container rse-organizer--gov">
            <div class="rse-organizer--header">
                <h4 class="rse-organizer--title">Gouvernance</h4>
            </div>
            <div class="rse-organizer--content">
                <div class="rse-organizer--esrs">
                    <button class="rse-organizer--card" title="Dérouler les sous-thèmes" aria-expanded="false" aria-controls="accordion-ESRS-G1">
                        <div class="rse-organizer--card-title">
                            <b>ESRS G1 - Conduite des affaires</b>
                        </div>
                        <div class="rse-organizer--card-themes">
                            <ul class="fr-collapse fr-text--sm" id="accordion-ESRS-G1">
                                <li>Culture d’entreprise</li>
                                <li>Protection des lanceurs d’alerte</li>
                                <li>Bien-être animal</li>
                                <li>Engagement politique</li>
                                <li>Gestion des relations avec les fournisseurs, y compris les pratiques en matière de paiement</li>
                                <li>Corruption et versement de pots-de-vin</li>
                                <li>
                                    <ul>
                                        <li>Prévention et détection, y compris les formations</li>
                                        <li>Incidents/Cas</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </button>
                    <button href="#" class="fr-btn fr-btn--sm fr-btn--secondary fr-icon-download-fill" title="Ouvre une modale de ressources à télécharger sur l'ESRS G1" aria-hidden="true" data-fr-opened="false" aria-controls="modal-ESRSG1"></button>
                </div>
            </div>
        </div>
    </div>
</div>
