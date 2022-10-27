# Generated by Django 4.1.1 on 2022-10-27 12:08

from django.db import migrations, models
import django.forms.fields
import reglementations.models


class Migration(migrations.Migration):

    dependencies = [
        ("reglementations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bdese_50_300",
            name="actions_emploi_personnes_handicapees",
            field=models.TextField(
                blank=True,
                help_text="Actions entreprises ou projetées en matière d'embauche, d'adaptation, de réadaptation ou de formation professionnelle",
                null=True,
                verbose_name="Actions entreprises ou projetées",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="actions_prevention_formation",
            field=models.TextField(
                blank=True,
                help_text="Indication des actions de prévention et de formation que l'employeur envisage de mettre en œuvre, notamment au bénéfice des salariés âgés, peu qualifiés ou présentant des difficultés sociales particulières",
                null=True,
                verbose_name="Actions de prévention et de formation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="affectation_benefices",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="L'affectation des bénéfices réalisés",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="aides_financieres",
            field=models.TextField(
                blank=True,
                help_text="Pour chacune de ces aides, l'employeur indique la nature de l'aide, son objet, son montant, les conditions de versement et d'emploi fixées, le cas échéant, par la personne publique qui l'attribue et son utilisation",
                null=True,
                verbose_name="Les aides ou avantages financiers consentis à l'entreprise par l'Union européenne, l'Etat, une collectivité territoriale, un de leurs établissements publics ou un organisme privé chargé d'une mission de service public, et leur utilisation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_ecarts_salaires",
            field=models.TextField(
                blank=True,
                help_text="En fonction de leur âge, de leur qualification et de leur ancienneté",
                null=True,
                verbose_name="Analyse des écarts de salaires et de déroulement de carrière",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_articulation_activite_pro_perso",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière d'articulation entre l'activité professionnelle et l'exercice de la responsabilité familiale",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_classification",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière de classification",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_conditions_de_travail",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière de conditions de travail",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_embauche",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière d'embauche",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_formation",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière de formation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_promotion_professionnelle",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière de promotion professionnelle",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_qualification",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière de qualification",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_remuneration",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière de rémunération effective",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="analyse_egalite_sante_et_sécurite",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Analyse chiffrée de la situation en matière de santé et de sécurité au travail",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="benefices_ou_pertes",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Les bénéfices ou pertes constatés"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="bilan_actions_plan_formation",
            field=models.TextField(
                blank=True,
                help_text="Le bilan des actions comprises dans le plan de formation de l'entreprise pour l'année antérieure et pour l'année en cours comportant la liste des actions de formation, des bilans de compétences et des validations des acquis de l'expérience réalisés, rapportés aux effectifs concernés répartis par catégorie socioprofessionnelle et par sexe",
                null=True,
                verbose_name="Bilan des actions comprises dans le plan de formation de l'entreprise",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="bilan_contrats_alternance",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Bilan, pour l'année antérieure et l'année en cours, des conditions de mise en œuvre des contrats d'alternance",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="bilan_cpf",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Bilan de la mise en œuvre du compte personnel de formation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="bilan_gaz_effet_de_serre",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Bilan des émissions de gaz à effet de serre prévu par l'article L. 229-25 du code de l'environnement ou bilan simplifié prévu par l'article 244 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021 pour les entreprises tenues d'établir ces différents bilans",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="cessions_fusions_acquisitions",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Cessions, fusions, et acquisitions réalisées",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="chiffre_affaires",
            field=models.IntegerField(
                blank=True, null=True, verbose_name=" Le chiffre d'affaires"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="conclusions_verifications_L_6361_1_L_6323_13_L_6362_4",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Conclusions éventuelles des services de contrôle faisant suite aux vérifications effectuées en application des articles L. 6361-1, L. 6323-13 et L. 6362-4",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="consommation_eau",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="consommation d'eau"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="consommation_energie",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="consommation d'énergie"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="credits_impots",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Crédits d'impôts"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="doeth",
            field=models.TextField(
                blank=True,
                help_text="Déclaration annuelle prévue à l'article L. 5212-5 à l'exclusion des informations mentionnées à l'article D. 5212-4",
                null=True,
                verbose_name="Déclaration obligatoire d'emploi des travailleurs handicapés",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_cdd",
            field=models.IntegerField(
                blank=True,
                help_text="Nombre de salariés titulaires d’un contrat de travail à durée déterminée",
                null=True,
                verbose_name="Effectif CDD",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_cdi",
            field=models.IntegerField(
                blank=True,
                help_text="Nombre de salariés titulaires d’un contrat de travail à durée indéterminée",
                null=True,
                verbose_name="Effectif CDI",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_femme",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField, blank=True, null=True
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_homme",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField, blank=True, null=True
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_mensuel",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=[
                    "Janvier",
                    "Février",
                    "Mars",
                    "Avril",
                    "Mai",
                    "Juin",
                    "Juillet",
                    "Aout",
                    "Septembre",
                    "Octobre",
                    "Novembre",
                    "Décembre",
                ],
                help_text="Evolution des effectifs retracée mois par mois",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_periode_professionnalisation_par_age",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=[
                    "moins de 30 ans",
                    "30 à 39 ans",
                    "40 à 49 ans",
                    "50 ans et plus",
                ],
                null=True,
                verbose_name="Effectifs intéressés par âge",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_periode_professionnalisation_par_niveau_initial",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["niveau I", "niveau II", "niveau III", "niveau IV"],
                null=True,
                verbose_name="Effectifs intéressés par niveau initial de formation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="effectif_periode_professionnalisation_par_sexe",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
                verbose_name="Effectifs intéressés par sexe",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="emplois_periode_professionnalisation",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Emplois occupés pendant et à l'issue de leur action ou de leur période de professionnalisation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="emprunts_et_dettes_financieres",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Emprunts et dettes financières dont échéances et charges financières",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="epargne_salariale",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Epargne salariale : intéressement, participation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="evolution_amortissement",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Evolution des actifs nets d’amortissement et de dépréciations éventuelles (immobilisations)",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="evolution_salariale_par_categorie",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField, blank=True, null=True
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="evolution_salariale_par_sexe",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="evolution_taux_promotion",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Description de l'évolution des taux de promotion respectifs des femmes et des hommes par métiers dans l'entreprise",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="exonerations_cotisations_sociales",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Exonérations et réductions de cotisations sociales",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="frais_personnel",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Frais de personnel, y compris cotisations sociales",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="horaires_temps_partiel",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Horaires de travail à temps partiel pratiqués dans l'entreprise",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="impots_et_taxes",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Impôts et taxes"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="informations_conges_formation",
            field=models.TextField(
                blank=True,
                help_text="Les informations, pour l'année antérieure et l'année en cours, relatives aux congés individuels de formation, aux congés de bilan de compétences, aux congés de validation des acquis de l'expérience et aux congés pour enseignement accordés ; notamment leur objet, leur durée et leur coût, aux conditions dans lesquelles ces congés ont été accordés ou reportés ainsi qu'aux résultats obtenus",
                null=True,
                verbose_name="Informations relatives aux congés de formation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="mecenat",
            field=models.IntegerField(blank=True, null=True, verbose_name="Mécénat"),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="mesures_methodes_production_exploitation",
            field=models.TextField(
                blank=True,
                help_text="et incidences de ces mesures sur les conditions de travail et l'emploi",
                null=True,
                verbose_name="Mesures envisagées en ce qui concerne l'amélioration, le renouvellement ou la transformation des méthodes de production et d'exploitation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="mesures_prises_egalite",
            field=models.TextField(
                blank=True,
                help_text="Bilan des actions de l'année écoulée et, le cas échéant, de l'année précédente. Evaluation du niveau de réalisation des objectifs sur la base des indicateurs retenus. Explications sur les actions prévues non réalisées",
                null=True,
                verbose_name="Mesures prises au cours de l'année écoulée en vue d'assurer l'égalité professionnelle",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="montant_contribution_activites_sociales_culturelles",
            field=models.IntegerField(
                blank=True,
                help_text="Du comité social et économique",
                null=True,
                verbose_name="Montant de la contribution aux activités sociales et culturelles",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="montant_depenses_recherche_developpement",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Dépenses de recherche et développement",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="montant_global_hautes_remunerations",
            field=models.IntegerField(
                blank=True,
                help_text="Montant global, certifié exact par les commissaires aux comptes, s'il en existe, des rémunérations versées aux personnes les mieux rémunérées, le nombre de ces personnes étant de dix ou de cinq selon que l'effectif du personnel excède ou non deux cents salariés ; uniquement pour les entreprises soumises aux dispositions de l'article L. 225-115 du code de commerce",
                null=True,
                verbose_name="Montant global des hautes rémunérations",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="motifs_contrats_cdd_temporaire_temps_partiel_exterieurs",
            field=models.TextField(
                blank=True,
                help_text="Motifs ayant conduit l'entreprise à recourir aux contrats de travail à durée déterminée, aux contrats de travail temporaire, aux contrats de travail à temps partiel, ainsi qu'à des salariés appartenant à une entreprise extérieure",
                null=True,
                verbose_name="Motifs",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_contrats_insertion_formation_jeunes",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Nombre de contrats d'insertion et de formation en alternance ouverts aux jeunes de moins de vingt-six ans",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_journees_salaries_temporaires",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Nombre de journées de travai réalisées au cours des douze derniers mois par les salariés temporaires",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_salaries_beneficaires_abondement",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Nombre des salariés bénéficiaires de l'abondement mentionné à l'avant-dernier alinéa du II de l'article L. 6315-1",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_salaries_beneficiaires_entretien_professionnel",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Nombre des salariés bénéficiaires de l'entretien professionnel mentionné au I de l'article L. 6315-1.",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_salaries_temporaires",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Nombre de salariés temporaires"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_salaries_temps_partiel_par_qualification",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Qualification des salariés travaillant à temps partiel",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_salaries_temps_partiel_par_sexe",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
                verbose_name="Nombre de salariés travaillant à temps partiel",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_stagiaires",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Nombre de stagiaires de plus de 16 ans",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="nombre_travailleurs_exterieurs",
            field=models.IntegerField(
                blank=True,
                help_text="Nombre de salariés appartenant à une entreprise extérieure",
                null=True,
                verbose_name="Nombre de travailleurs extérieurs",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="objectifs_progression",
            field=models.TextField(
                blank=True,
                help_text="Définition qualitative et quantitative des mesures permettant de les atteindre conformément à l'article R. 2242-2. Evaluation de leur coût. Echéancier des mesures prévues",
                null=True,
                verbose_name="Objectifs de progression pour l'année à venir et indicateurs associés",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="orientations_formation_professionnelle",
            field=models.TextField(
                blank=True,
                help_text="Les orientations de la formation professionnelle dans l'entreprise telles qu'elles résultent de la consultation prévue à l'article L. 2312-24",
                null=True,
                verbose_name="Orientations de la formation professionnelle",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="partenariats_pour_beneficier",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Partenariats conclus pour bénéficier des services ou des produits d'une autre entreprise",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="partenariats_pour_produire",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Partenariats conclus pour produire des services ou des produits pour une autre entreprise",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="postes_emissions_directes_gaz_effet_de_serre",
            field=models.TextField(
                blank=True,
                help_text="produites par les sources fixes et mobiles nécessaires aux activités de l'entreprise (communément appelées \"émissions du scope 1\") et, lorsque l'entreprise dispose de cette information, évaluation du volume de ces émissions de gaz à effet de serre ",
                null=True,
                verbose_name="Identification des postes d'émissions directes de gaz à effet de serre",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="prise_en_compte_questions_environnementales",
            field=models.TextField(
                blank=True,
                help_text="et, le cas échéant, les démarches d'évaluation ou de certification en matière d'environnement",
                null=True,
                verbose_name="Organisation de l'entreprise pour prendre en compte les questions environnementales",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="programme_prevention_risques_pro",
            field=models.TextField(
                blank=True,
                help_text="prévu au 2° de l'article L. 2312-27 établi à partir des analyses mentionnées à l'article L. 2312-9 et fixant la liste détaillée des mesures devant être prises au cours de l'année à venir dans les mêmes domaines afin de satisfaire, notamment :\n            i-Aux principes généraux de prévention prévus aux articles L. 4121-1 à L. 4121-5 et L. 4221-1 ;\n            ii-A l'information et à la formation des travailleurs prévues aux articles L. 4141-1 à L. 4143-1 ;\n            iii-A l'information et à la formation des salariés titulaires d'un contrat de travail à durée déterminée et des salariés temporaires prévues aux articles L. 4154-2 et L. 4154-4 ;\n            iv-A la coordination de la prévention prévue aux articles L. 4522-1 et L. 4522-2 ;\n        ",
                null=True,
                verbose_name="Programme annuel de prévention des risques professionnels et d'amélioration des conditions de travail",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="quantite_de_dechets_dangereux",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="évaluation de la quantité de déchets dangereux définis à l'article R. 541-8 du code de l'environnement et faisant l'objet d'une émission du bordereau mentionné à l'article R. 541-45 du même code",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="reductions_impots",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Réductions d'impôts"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="remuneration_actionnaires",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Rémunération des actionnaires (revenus distribués)",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="remuneration_actionnariat_salarie",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Rémunération de l'actionnariat salarié (montant des actions détenues dans le cadre de l'épargne salariale, part dans le capital, dividendes reçus)",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="resultat_negociations_L_2241_6",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Résultat éventuel des négociations prévues à l'article L. 2241-6",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="resultats_globaux",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["valeur", "volume"],
                null=True,
                verbose_name="Les résultats globaux de la production",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="resultats_periode_professionnalisation",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Résultats obtenus en fin d'action ou de période de professionnalisation ainsi que les conditions d'appréciation et de validation",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="salaire_base_minimum_par_categorie",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Salaire de base minimum par catégorie",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="salaire_base_minimum_par_sexe",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
                verbose_name="Salaire de base minimum par sexe",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="salaire_median_par_categorie",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Salaire médian par catégorie",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="salaire_median_par_sexe",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
                verbose_name="Salaire médian par sexe",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="salaire_moyen_par_categorie",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Salaire moyen par catégorie",
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="salaire_moyen_par_sexe",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="somme_abondement",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Sommes versées à ce titre"
            ),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="transferts_de_capitaux",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Transferts de capitaux tels qu'ils figurent dans les comptes individuels des sociétés du groupe lorsqu'ils présentent une importance significative",
            ),
        ),
    ]
