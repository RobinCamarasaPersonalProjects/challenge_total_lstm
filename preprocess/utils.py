import csv
import numpy as np


def normalize_X(array, nb_exp):
    if nb_exp == 1:
        extremums = [[1001669.0, 1001794.0], [1001663.0, 1001739.0], [1001639.0, 1001692.0], [267.85, 302.25],
                     [0.0, 101.0], [-0.1, 11.9], [0.0, 10.5], [269.15, 308.75], [0.0, 101.0], [-0.1, 13.1], [0.0, 12.1],
                     [267.95, 302.35], [0.0, 101.0], [-0.1, 7.7], [0.0, 11.8], [270.25, 308.85], [0.0, 101.0],
                     [-0.1, 26.9], [0.0, 11.2], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0],
                     [0.0, 2.0], [0.0, 2.0], [0.0, 2.0], [0.0, 2.0], [0.0, 2.0], [0.0, 3.0], [0.0, 31.03], [0.0, 90.11],
                     [0.0, 15.9], [0.0, 40.3], [0.0, 4.71], [0.0, 13.7], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                     [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 3.0], [0.0, 203.0],
                     [0, 366]]
    else:
        extremums = [[1001669.0, 1001794.0], [1001663.0, 1001739.0], [1001639.0, 1001692.0], [267.85, 302.25],
                     [0.0, 101.0], [-0.1, 11.9], [0.0, 10.5], [269.15, 308.75], [0.0, 101.0], [-0.1, 13.1], [0.0, 12.1],
                     [267.95, 302.35], [0.0, 101.0], [-0.1, 7.7], [0.0, 11.8], [270.25, 308.85], [0.0, 101.0],
                     [-0.1, 26.9], [0.0, 11.2], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0], [0.0, 3.0],
                     [0.0, 2.0], [0.0, 2.0], [0.0, 2.0], [0.0, 2.0], [0.0, 2.0], [0.0, 3.0], [0.0, 17.86], [0.0, 68.52],
                     [0.0, 6.18], [0.0, 23.0], [0.0, 1.87], [0.0, 7.89], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0],
                     [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 3.0], [0.0, 203.0],
                     [0, 366]]
    i = 0
    for (min, max) in extremums:
        if min != max:
            array[i, :, :] = (array[i, :, :] - min) / (max - min)
        i += 1


def normalize_Y(array, nb_exp):
    i = 0
    if nb_exp == 1:
        extremums = [[0.0, 6.68], [0.0, 6.23], [0.0, 8.31], [0.0, 6.23], [0.0, 2.32], [0.0, 6.78], [0.0, 4.15],
                     [0.0, 8.95],
                     [0.0, 12.73], [0.0, 2.02], [0.0, 14.46], [0.0, 12.87], [0.0, 13.29], [0.0, 9.14], [0.0, 6.64],
                     [0.0, 7.47], [0.0, 2.49], [0.0, 4.57], [0.0, 3.24], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                     [0.0, 2.32],
                     [0.0, 0.0], [0.0, 2.78], [0.0, 2.78], [0.0, 2.32], [0.0, 4.63], [0.0, 0.0], [0.0, 0.0],
                     [0.0, 4.63],
                     [0.0, 3.24], [0.0, 4.63], [0.0, 9.73], [0.0, 1.29], [0.0, 5.17], [0.0, 7.89], [0.0, 8.2],
                     [0.0, 7.96],
                     [0.0, 1.85], [0.0, 2.6], [0.0, 3.15], [0.0, 2.23], [0.0, 5.75], [0.0, 2.6], [0.0, 2.04],
                     [0.0, 4.97],
                     [0.0, 10.01], [0.0, 6.48], [0.0, 3.71], [0.0, 3.71], [0.0, 4.17], [0.0, 3.71], [0.0, 12.51],
                     [0.0, 7.41], [0.0, 5.09], [0.0, 7.87], [0.0, 6.48], [0.0, 7.41], [0.0, 4.17], [0.0, 3.32],
                     [0.0, 1.39],
                     [0.0, 3.15], [0.0, 5.09], [0.0, 3.52], [0.0, 6.02], [0.0, 12.51], [0.0, 10.35], [0.0, 12.07],
                     [0.0, 5.61], [0.0, 7.06], [0.0, 3.32], [0.0, 3.74], [0.0, 11.21], [0.0, 2.32], [0.0, 2.78],
                     [0.0, 1.85], [0.0, 0.0], [0.0, 8.62], [0.0, 2.71], [0.0, 9.49], [0.0, 4.74], [0.0, 10.76],
                     [0.0, 31.03], [0.0, 6.48], [0.0, 6.02], [0.0, 5.4], [0.0, 4.98], [0.0, 4.15], [0.0, 0.0],
                     [0.0, 5.09],
                     [0.0, 8.34], [0.0, 5.56], [0.0, 4.63], [0.0, 2.49], [0.0, 1.48], [0.0, 5.93], [0.0, 3.78],
                     [0.0, 12.98], [0.0, 5.01], [0.0, 3.52], [0.0, 7.79], [0.0, 6.48], [0.0, 11.12], [0.0, 6.04],
                     [0.0, 10.46], [0.0, 6.05], [0.0, 15.28], [0.0, 0.0], [0.0, 6.78], [0.0, 4.07], [0.0, 0.9],
                     [0.0, 8.14],
                     [0.0, 23.16], [0.0, 23.62], [0.0, 26.4], [0.0, 6.78], [0.0, 6.47], [0.0, 5.17], [0.0, 0.0],
                     [0.0, 2.91], [0.0, 4.15], [0.0, 0.0], [0.0, 4.57], [0.0, 9.49], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                     [0.0, 2.49], [0.0, 0.0], [0.0, 4.29], [0.0, 5.29], [0.0, 1.01], [0.0, 6.3], [0.0, 7.06],
                     [0.0, 5.93],
                     [0.0, 5.67], [0.0, 4.54], [0.0, 5.55], [0.0, 4.29], [0.0, 5.67], [0.0, 6.88], [0.0, 5.91],
                     [0.0, 5.31],
                     [0.0, 5.31], [0.0, 11.7], [0.0, 4.7], [0.0, 4.1], [0.0, 8.32], [0.0, 8.93], [0.0, 4.83],
                     [0.0, 6.18],
                     [0.0, 7.44], [0.0, 9.17], [0.0, 8.81], [0.0, 6.51], [0.0, 3.5], [0.0, 7.96], [0.0, 4.1],
                     [0.0, 4.22],
                     [0.0, 3.86], [0.0, 5.55], [0.0, 3.62], [0.0, 9.77], [0.0, 3.26], [0.0, 3.14], [0.0, 7.69],
                     [0.0, 3.77],
                     [0.0, 4.86], [0.0, 2.78], [0.0, 2.32], [0.0, 1.85], [0.0, 7.06], [0.0, 7.06], [0.0, 20.76],
                     [0.0, 18.27], [0.0, 2.32], [0.0, 2.41], [0.0, 3.89], [0.0, 3.32], [0.0, 7.68], [0.0, 10.35],
                     [0.0, 10.99], [0.0, 5.09], [0.0, 6.04], [0.0, 8.32], [0.0, 8.94], [0.0, 13.43], [0.0, 19.45],
                     [0.0, 3.71], [0.0, 6.48], [0.0, 6.95], [0.0, 4.17], [0.0, 6.95], [0.0, 10.19], [0.0, 3.24],
                     [0.0, 8.34], [0.0, 8.34], [0.0, 5.56], [0.0, 5.09], [0.0, 6.48], [0.0, 3.71], [0.0, 9.26],
                     [0.0, 4.63]]
    else:
        extremums = [[0.0, 2.04], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 3.24], [0.0, 0.0], [0.0, 2.08], [0.0, 0.0],
                     [0.0, 0.0], [0.0, 0.0], [0.0, 7.68], [0.0, 8.31], [0.0, 3.74], [0.0, 3.74], [0.0, 3.74],
                     [0.0, 5.4], [0.0, 0.0], [0.0, 1.66], [0.0, 0.0], [0.0, 3.71], [0.0, 3.74], [0.0, 1.39],
                     [0.0, 1.39], [0.0, 1.39], [0.0, 1.85], [0.0, 4.17], [0.0, 1.39], [0.0, 1.85], [0.0, 2.16],
                     [0.0, 3.71], [0.0, 1.85], [0.0, 3.24], [0.0, 2.32], [0.0, 4.63], [0.0, 0.0], [0.0, 4.31],
                     [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.93], [0.0, 0.0], [0.0, 0.0], [0.0, 1.3], [0.0, 2.23],
                     [0.0, 1.11], [0.0, 0.74], [0.0, 0.0], [0.0, 0.0], [0.0, 2.32], [0.0, 0.0], [0.0, 2.78],
                     [0.0, 1.85], [0.0, 2.32], [0.0, 4.17], [0.0, 0.0], [0.0, 3.71], [0.0, 3.71], [0.0, 3.24],
                     [0.0, 4.63], [0.0, 2.32], [0.0, 2.08], [0.0, 2.32], [0.0, 1.48], [0.0, 3.24], [0.0, 1.11],
                     [0.0, 3.71], [0.0, 3.45], [0.0, 4.31], [0.0, 3.02], [0.0, 1.29], [0.0, 2.08], [0.0, 6.23],
                     [0.0, 0.0], [0.0, 3.32], [0.0, 3.24], [0.0, 2.78], [0.0, 2.32], [0.0, 2.32], [0.0, 0.0],
                     [0.0, 0.0], [0.0, 0.0], [0.0, 1.29], [0.0, 2.04], [0.0, 4.17], [0.0, 0.0], [0.0, 6.02], [0.0, 0.0],
                     [0.0, 2.08], [0.0, 0.0], [0.0, 4.15], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
                     [0.0, 0.93], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 1.67], [0.0, 1.11], [0.0, 2.23],
                     [0.0, 8.34], [0.0, 4.17], [0.0, 2.16], [0.0, 0.0], [0.0, 0.0], [0.0, 6.02], [0.0, 4.17],
                     [0.0, 0.45], [0.0, 3.62], [0.0, 1.81], [0.0, 0.45], [0.0, 10.19], [0.0, 8.8], [0.0, 6.48],
                     [0.0, 5.42], [0.0, 2.59], [0.0, 0.0], [0.0, 1.25], [0.0, 0.0], [0.0, 0.0], [0.0, 2.08], [0.0, 0.0],
                     [0.0, 0.0], [0.0, 2.26], [0.0, 2.71], [0.0, 1.81], [0.0, 0.0], [0.0, 2.08], [0.0, 2.27],
                     [0.0, 2.14], [0.0, 0.0], [0.0, 1.64], [0.0, 3.4], [0.0, 1.26], [0.0, 0.0], [0.0, 3.4], [0.0, 0.25],
                     [0.0, 2.52], [0.0, 1.57], [0.0, 2.17], [0.0, 3.02], [0.0, 3.38], [0.0, 3.38], [0.0, 4.58],
                     [0.0, 5.07], [0.0, 2.41], [0.0, 4.22], [0.0, 5.55], [0.0, 0.0], [0.0, 6.18], [0.0, 4.79],
                     [0.0, 3.86], [0.0, 5.91], [0.0, 4.22], [0.0, 1.45], [0.0, 4.95], [0.0, 0.0], [0.0, 2.9],
                     [0.0, 0.0], [0.0, 2.17], [0.0, 0.0], [0.0, 0.84], [0.0, 3.02], [0.0, 1.88], [0.0, 2.35],
                     [0.0, 2.67], [0.0, 0.63], [0.0, 2.78], [0.0, 3.24], [0.0, 1.85], [0.0, 2.49], [0.0, 4.15],
                     [0.0, 4.98], [0.0, 17.86], [0.0, 1.85], [0.0, 0.74], [0.0, 0.93], [0.0, 1.66], [0.0, 0.0],
                     [0.0, 1.29], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 4.17], [0.0, 3.71],
                     [0.0, 0.0], [0.0, 2.32], [0.0, 2.78], [0.0, 0.0], [0.0, 0.0], [0.0, 4.17], [0.0, 2.78],
                     [0.0, 3.24], [0.0, 3.24], [0.0, 2.32], [0.0, 3.71], [0.0, 3.24], [0.0, 3.71], [0.0, 3.24],
                     [0.0, 3.24]]
    k = 0
    for (min, max) in extremums:
        if min != max:
            array[0, :, k] = (array[0, :, k] - min) / (max - min)
        k += 1


def create_X(nb_exp, type, path, path_csv, nb_days, nb_features, nb_products):
    products = ['12_Baguette_Viennoise_X2_170G_La_Boulangere', '4Tr_Blanc_De_Poulet_160G_Dm', '4_Tr_Jb_Italien_120G_Dm',
                '4_Trs_Filet_Plt_Roti_120G_Dm', 'Actimel_100G_Danone', 'Ananas_Mcx_200G_Dm',
                'Assiette_Francaise_80G_Sapresti', 'Baguette_Jambon_Crudites_255G_Dm',
                'Baguette_Poulet_Crudites_250G_Dm',
                'Baguette_Thon_Basilic_235G_Dm', 'Banane_X2_200G_Vdumay', 'Baton_Berger_Mini_Nature_80G_Jb',
                'Baton_Berger_Mini_Noix_80G_Jb', 'Baton_Berger_Mini_Piment_Doux_80G_Jb',
                'Baton_Berger_Mini_Poulet_100G_Jb',
                'Baton_Berger_Nature_75G_Jb', 'Baton_Berger_Rondelles_120G_Jb', 'Batonnets_Coraya_Saveur_100G_Aoc',
                'Beurre_Doux_125G_President_Dm', 'Beurrier_Tendre_125G_President', 'Blanc_De_Poulet_2T_80G_Casino',
                'Boissons_Lactees_350Ml_Bounty', 'Boissons_Lactees_350Ml_Mars', 'Boissons_Lactees_350Ml_Mms',
                'Boissons_Lactees_350Ml_Snickers', 'Brie_200G_Casino', 'Cafe_Royal_Caramel_230Ml_Mifroma',
                'Cafe_Royal_Extra_Strong_230Ml_Mifroma', 'Cake_Jambon_Olives_120G_Daunat', 'Camembert_250G_Casino',
                'Camembert_Coeur_De_Lion_150G', 'Camembert_Coeur_De_Lion_X8_240G', 'Candy_Up_Chocolat_1L_Candia',
                'Candy_Up_Chocolat_50Cl', 'Carrement_Tarte_Chevre_Tomate_190G', 'Cheese_Burger_145G_Charal',
                'Chorizo_10_Tr_70G_Dm', 'Club_Jmb_Emmental_135G_Dm', 'Club_Trio_Jmb_Plt_Fro_225G_Dm',
                'Cookie_70G_Daunat',
                'Cookie_Cara_Noix_Pecan_70G_Michel_Augustin', 'Cookie_Choc_Blc_70G_Michel_Augustin',
                'Cookie_Choc_Nois_70G_Michel_Augustin', 'Cookie_Choco_70G_Michel_Augustin',
                'Crepe_Chocolat_130G_Daunat',
                'Crepe_Pomme_150G_Daunat', 'Croc_Pomme_Raisin_80G_Dm', 'Croissant_60G_Cuit/Place_Neuhauser',
                'Danio_Fraise_150G_Danone', 'Danio_Framboise_150G_Danone', 'Danio_Myrtille_150G_Danone',
                'Danio_Passion_150G_Danone', 'Danio_Vanille_150G_Danone', 'Danonino_Fraise_100G',
                'Des_Fromages_Hollande_150G_Dm', 'Discoveries_Americano_22Cl_Starbucks',
                'Discoveries_Cap_22Cl_Starbuck',
                'Discoveries_Caramel_22Cl_Starbucks', 'Discoveries_Seattle_22Cl_Starbucks',
                'Doubleshot_Exp_200Ml_Starbucks',
                'Duo_Campagne_+_Canard_2X50G_Madrange', 'Emmental_Tranches_Entremont_150G',
                'Flan_Patissier_120G_Daunat',
                'Fol_Epi_7Tr_150G', 'Fondant_Au_Chocolat_90G_Daunat', 'Frappuccino_Cof_25Cl_Starbucks',
                'Fusilli_Bolo_300G_Sodebo', 'Fusilli_Carbo_300G_Sodebo', 'Fusilli_From_Itln_300G_Sodebo',
                'Hot_Dog_Ketchup_120G_Charal', 'Jambon_Cru_4T_50G_Aoste', 'Jambon_Paris_2T_Dd_80G_Casino',
                'Jambon_Serrano_80G_Dm', 'Justun_Delice_Mini_80G', 'Lait_12_Ecreme_Nature_1L_Casino',
                'Lait_12_Ecreme_Nature_50Cl_Casino', 'Mamie_Nova_Chocolat_150G', 'Mamie_Nova_Vanille_150G',
                'Manchons_Poulet_Nat_250G_Dm', 'Mangue_200G_Dm', 'Maxi_Cheese_220G_Charal', 'Maxi_Hot_Dog_160G_Charal',
                'Maxi_Pain_Choco_75G_Boulangere', 'Mini_Babybel_X4_88G_Bel', 'Mini_Caprice_Des_Dieux_150G',
                'Mini_Caprice_Des_Dieux_50G', 'Mini_Saucisson_75G_Dm', 'Mini_Saucisson_90G_Bordeau_Chesnel',
                'Mini_Saucisson_Aux_Noix_75G_Dm', 'Mon_Jambon_Blanc_2T_80G_Madrange', 'Monop_Pointe_De_Brie_200G',
                'Monop_Tranche_Gouda_200G_Dm', 'Monop_Tranche_Mimolette_200G_Dm', 'Mousse_Choco_80G_Dm',
                'Mousse_De_Canard_2X50G_Madrange', 'Muffin_115G_Daunat', 'Navette_Jambon_Beurre_85G_Dm',
                'Navette_Poulet_Concombre_105G_Dm', 'Pain_Chocolat_60G_Cuit/Place_Neuhauser',
                'Pain_De_Campagne_400G_La_Boulangere', 'Pain_Mie_Extra_Moel_280G_Casino', 'Pain_Raisins_70G_Boulangere',
                'Panier_Quartier_Fraise_150G_Yoplait', 'Panier_Quartiers_Peche_150G_Yoplait',
                'Pave_Charolais_180G_Daunat',
                'Pave_Jambon_Emmental_210G_Dm', 'Pave_Poulet_Crudites_225G_Dm', 'Petits_Filous_Fraise_80G_Yoplait',
                'Pikcroq_Duo_70G_Bel', 'Pom_Golden_Unite_90G_Vdumay', 'Pom_Golden_X2_280G_Vdumay',
                'Pommes_X4_560G_Vdumay',
                'Pom_Panache_X2_280G_Vdumay', 'Pompotes_Pomme_Fraise_90G_Materne', 'Pompotes_Pomme_Nature_90G_Materne',
                'Pompotes_Pom_S_Sucre_90G_Materne', 'Pom_Rouge_X2_280G_Vdumay', 'Radiatori_Boeuf_Poivre_400G_Sodebo',
                'Radiatori_Carbo_400G_Sodebo', 'Rillettes_Poulet_110G', 'Rillettes_Pp_Sans_Graisse_220G_Dm',
                'Rosette_10_Trs_100G_Dm', 'Rosette_15Tr_150G_Casino', 'Roti_De_Porc_X2_100G_Fleury_Michon',
                'Salade_De_Fruits_200G_Dm', 'Salade_Fruits_Ananas_198G_Dole', 'Salade_Fruits_Peche_198G_Dole',
                'Salade_Fruits_Tropicaux_198G_Dole', 'Saucisse_Seche_Pp_250G_Monoprix',
                'Saucisses_Stras_X4_140G_Casino',
                'Sdw_Bag_Camp_Jamb_Emm_220G_Daunat', 'Sdw_Bag_Camp_Poulet_Roti_220G_Daunat',
                'Sdw_Bag_Camp_Rosette_Cornichon_220G_Daunat', 'Sdw_Bag_Mega_Jamb_Cheddar_270G_Sodebo',
                'Sdw_Bag_Mega_Poulet_Oeuf_Toma_270G_Sodebo', 'Sdw_Bag_Mega_Thon_Oeuf_Cockta_270G_Sodebo',
                'Sdw_Bag_Vien_Jamb_Emm_230G_Daunat', 'Sdw_Bag_Vien_Jb_Salami_Emm_215G_Daunat',
                'Sdw_Bag_Vien_Poulet_Crud_230G_Daunat', 'Sdw_Bag_Vien_Thon_Oeuf_Crud_230G_Daunat',
                'Sdw_Chevre_Concombre_160Gr_Daunature', 'Sdw_Gourmand_Jambon_Cheddar_190G_Sodebo',
                'Sdw_Gourmand_Jambon_Cru_190G_Sodebo', 'Sdw_Gourmand_Poulet_Caesar_190G_Sodebo',
                'Sdw_Gourmand_Saumon_Fume_190G_Sodebo', 'Sdw_Jamb_Beurre_125G_Sodebo', 'Sdw_Jambon_Cheddar_230G_Xxl',
                'Sdw_Jambon_Comte_160G_Daunature', 'Sdw_Jambon_Emm_230G_Xxl', 'Sdw_Jambon_Emmental_160G_Daunat',
                'Sdw_Le_Maxi_Club_255G_Dm', 'Sdw_Mini_Jambon_Emm_130G_Daunat', 'Sdw_Mini_Poulet_Emm_130G_Daunat',
                'Sdw_Poulet_Roti_125G_Simple_Sodebo', 'Sdw_Poulet_Roti_Crud_230G_Xxl',
                'Sdw_Poulet_Roti_Mayo_160G_Daunat',
                'Sdw_Poulet_Roti_Parmesan_160G_Daunature', 'Sdw_Rosette_125G_Sodebo',
                'Sdw_Rosette_Beurre_Cornich_230G_Xxl',
                'Sdw_Suedois_Duo_Saumon_135G_Sodebo', 'Sdw_Suedois_Jambon_Cru_Emme_135G_Sodebo',
                'Sdw_Suedois_Jb_Cheddar_135G_Sodebo', 'Sdw_Thon_Crud_230G_Xxl', 'Sdw_Thon_Crudites_125G_Simple_Sodebo',
                'Sdw_Thon_Crudites_160G_Daunat', 'Sdw_Wrap_Duo_Saumon_190G_Daunat',
                'Sdw_Wrap_Jambon_Brebis_190G_Daunat',
                'Sdw_Wrap_Poulet_Fajitas_190G_Daunat', 'Sdw_Wrap_Poulet_Roti_Tom_190G_Daunat',
                'Shakissimo_Latte_Cappucino_190Ml_Nescafe', 'Shakissimo_Latte_Expresso_190Ml_Nescafe',
                'Shakissimo_Latte_Macchiato_190Ml_Nescafe', 'Sticks_Chorizo_100G_Auvernou',
                'Sticks_Roquefort_100G_Auvernou',
                'Sticks_Saucisson_100G_Auvernou', 'Sticks_Saucisson_X3_30G_Auvernou', 'Tartare_6P_96G_Afs',
                'Tarte_Au_Citron_90G_Daunat', 'Tarte_Normande_Aux_Pommes_100G_Daunat',
                'Terrine_De_Campagne_X2_100G_Madrange', 'Tomates_Cerise_250G_Vdumay', 'Tortellini_Ricota_280G_Sodebo',
                'Trio_Wraps_Poulet_320G_Dm', 'Vache_Qui_Rit_8P_170G', 'Very_Best_220G_Charal',
                'Wrap_Poulet_Basilic_200G_Dm',
                'Wrap_Poulet_Ceasar_205G_Dm', 'Yab_Chataigne_25Cl_Daunature', 'Yab_Vanille_25Cl_Daunature',
                'Yaourt_Caramel_Et_Sel_150G_Dm', 'Yaourt_Framboise_25Cl_Michel_Augustin',
                'Yaourt_Mang_Pas_25Cl_Michel_Augustin', 'Yaourt_Myrtille_25Cl_Michel_Augustin',
                'Yaourt_Vanille_0_150G_Dm',
                'Yaourt_Vanille_25Cl_Michel_Augustin', 'Yop_850G_Tropical_Fresh_850G_Yoplait',
                'Yop_Fraise_250G_Yoplait',
                'Yop_Fraise_500G_Yoplait', 'Yop_Fraise_850G_Yoplait', 'Yop_Framboise_250G_Yoplait',
                'Yop_Framboise_500G_Yoplait', 'Yop_Framboise_850G_Yoplait', 'Yop_Vanille_500G_Yoplait',
                'Yop_Vanille_850G_Yoplait']
    X = np.zeros(nb_days * nb_features * nb_products).reshape(nb_features, nb_days, nb_products)
    number_data = [4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                   33,
                   34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
    nb_line = -1
    with open(path_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            if nb_line >= 0:
                for i, index in enumerate(number_data):
                    j, k = nb_line % nb_days, nb_line / nb_days
                    X[i][j][k] = float(row[index])
                X[len(number_data)][j][k] = float(products.index(row[3]))
                X[len(number_data) + 1][j][k] = float(int(row[55]) % 366)
            nb_line += 1
        normalize_X(X, nb_exp)
    np.save(path + 'X_' + type + '_' + str(nb_exp) + '.npy', X)


def create_Y(nb_exp, type, path, path_csv, nb_days, nb_products):
    Y = np.zeros(nb_days * nb_products).reshape(1, nb_days, nb_products)
    nb_line = -1
    with open(path_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            if nb_line >= 0:
                j, k = nb_line % nb_days, nb_line / nb_days
                Y[0][j][k] = float(row[56])
            nb_line += 1
        normalize_Y(Y, nb_exp)
    np.save(path + 'Y_' + type + '_' + str(nb_exp) + '.npy', Y)
    print('end')
