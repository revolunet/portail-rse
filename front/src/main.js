import DenominationEntreprise from './lib/DenominationEntreprise.svelte'
import ExternalFieldToggle from './lib/ExternalFieldToggle.svelte'
import GroupeFields from './lib/GroupeFields.svelte'
import InteretPublicField from './lib/InteretPublicField.svelte'
import SimulationForm from './lib/SimulationForm.svelte'
import SearchEntreprise from './lib/SearchEntreprise.svelte'
import SeeMoreOrLess from './lib/SeeMoreOrLess.svelte'
import ThemesRapportDurabilite from './lib/ThemesRapportDurabilite.svelte'

for (let externalFieldToggle of document.getElementsByClassName("svelte-external-field-toggle")) {
  new ExternalFieldToggle({
    target: externalFieldToggle,
    props: {
      toggleId: externalFieldToggle.dataset.toggleId,
      fieldName: externalFieldToggle.dataset.fieldName,
      fieldContainerId: externalFieldToggle.dataset.fieldContainerId,
      externalFieldsInStepFieldId: externalFieldToggle.dataset.externalFieldsInStepFieldId
    }
  })
}


const searchEntrepriseElement = document.getElementById("svelte-search-entreprise")
if (searchEntrepriseElement) {
  new SearchEntreprise({
    target: searchEntrepriseElement,
    props: {
      siren: searchEntrepriseElement.dataset.siren,
      denomination: searchEntrepriseElement.dataset.denomination
    },
    hydrate: true,
  })
}

const appartientGroupeFieldElement = document.getElementById("svelte-appartient-groupe-field")
if (appartientGroupeFieldElement) {
  new GroupeFields({
    target: appartientGroupeFieldElement,
  })
}

const estInteretPublicFieldElement = document.getElementById("svelte-est-interet-public-field")
if (estInteretPublicFieldElement) {
  new InteretPublicField({
    target: estInteretPublicFieldElement,
  })
}

const simulationFormElement = document.getElementById("svelte-search-entreprise-in-simulation-form")
if (simulationFormElement) {
  new SimulationForm({
    target: simulationFormElement,
    props: {
      siren: simulationFormElement.dataset.siren,
      denomination: simulationFormElement.dataset.denomination
    },
    hydrate: true,
  })
}

const denominationEntrepriseElement = document.getElementById("svelte-denomination-entreprise")
if (denominationEntrepriseElement) {
  new DenominationEntreprise({
    target: denominationEntrepriseElement,
    props: {
      denomination: denominationEntrepriseElement.dataset.denomination
    },
    hydrate: true,
  })
}

const voirPlusMoinsElement = document.getElementById("svelte-voir-plus-moins")
if (voirPlusMoinsElement) {
  new SeeMoreOrLess({
    target: voirPlusMoinsElement
  })
}

const themesRapportDurabilite = document.getElementById("svelte-themes-rapport-durabilite")
if (themesRapportDurabilite) {
  new ThemesRapportDurabilite({
    target: themesRapportDurabilite
  })
}
