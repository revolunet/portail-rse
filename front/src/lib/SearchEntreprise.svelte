<script>
    import spinner from './assets/spinner.svg'
    import DenominationEntreprise from './DenominationEntreprise.svelte';

    export let siren = ""
    export let denomination = ""
    let loading = false
    let promise = async () => {}

    // defined by django
    const sirenFieldId = "id_siren"
    const sirenFieldName = "siren"
    const denominationFieldName = "denomination"

    const denominationEntrepriseElement = document.getElementById("svelte-denomination-entreprise")
    const submitButton = document.getElementById(sirenFieldId).closest("form").querySelector("[type=submit]")
    const sirenTest = "000000001"
    const infosEntrepriseTest = {
        "siren": sirenTest,
        "denomination": "ENTREPRISE TEST",
        "effectif": "10000+",
        "categorie_juridique_sirene": 5505,
        "code_pays_etranger_sirene": null,
        "code_NAF": "01.11Z",
        "date_cloture_exercice": "2023-12-31",
        "tranche_chiffre_affaires": "100M+",
        "tranche_chiffre_affaires_consolide": null
    }

    async function searchEntreprise(siren) {
        if (siren.length !== 9 || isNaN(siren)){
            const event = new CustomEvent("siren-incorrect")
            document.dispatchEvent(event)
            throw new Error("Le siren est incorrect.")
        } else if (siren === sirenTest){
            // on permet la recherche d'une entreprise fictive de test pour des utilisateurs potentiels qui n'ont pas d'entreprise
            // mais qui souhaitent tester le portail et s'inscrire avec cette entreprise test, comme les étudiants par exemple
            submitButton.disabled = false
            denomination = infosEntrepriseTest.denomination
            const event = new CustomEvent("infos-entreprise", {detail: infosEntrepriseTest})
            document.dispatchEvent(event)
        } else {
            loading = true
            const res = await fetch("/api/search-entreprise/" + siren)
            const json = await res.json()

            if (res.ok) {
                loading = false
                submitButton.disabled = false
                denomination = json.denomination
                const event = new CustomEvent("infos-entreprise", {detail: json})
                document.dispatchEvent(event)
            } else {
                loading = false
                const event = new CustomEvent("siren-incorrect")
                document.dispatchEvent(event)
                throw new Error(json['error'])
            }
        }
    }

    const handleChange = () => {
        submitButton.disabled = true
        promise = searchEntreprise(siren)
    }

    if (!siren) {
        submitButton.disabled = true
    }
    else if (!denomination) {
        handleChange()
    }
</script>

<fieldset class="fr-fieldset" aria-label="SIREN de l'entreprise">
    <div class="fr-fieldset__element">
        <div class="fr-input-group">
            <label class="fr-label" for="{sirenFieldId}">Saisissez le numéro SIREN de votre entreprise</label>
            <div class="fr-col-12 fr-col-sm-6 fr-mt-1w">
                <div class="fr-search-bar" role="search">
                {#if ! loading}
                    <input type="search" name="{sirenFieldName}" maxlength="9" minlength="9" class="fr-input" id="{sirenFieldId}" required bind:value={siren} on:change|preventDefault={handleChange}>
                    <button type="button" class="fr-btn" title="Rechercher" on:click|preventDefault={handleChange}>
                        Rechercher
                    </button>
                {:else}
                    <input type="text" name="{sirenFieldName}" maxlength="9" minlength="9" class="fr-input" id="{sirenFieldId}" value="{siren}" readonly>
                    <img src="{spinner}" width="40" alt="Spinner d'attente">
                {/if}
                </div>
            </div>
            <div class="fr-my-1w">
                <a class="fr-link" target="_blank" rel="noopener noreferrer" href="https://annuaire-entreprises.data.gouv.fr/">
                    Trouvez votre SIREN sur l'Annuaire des entreprises
                </a>
            </div>
            {#await promise then result}
            {:catch error}
                <p class="fr-error-text">{error.message}</p>
            {/await}
            {#if !denominationEntrepriseElement}
                <DenominationEntreprise />
            {/if}
        </div>
    </div>
</fieldset>

<input type="hidden" name="{denominationFieldName}" value="{denomination}">
