import csv
import numpy as np


def normalize(array, line):
    if array[line, :].min() != array[line, :].max():
        array[line, :] = (array[line, :] - array[line, :].min())/(array[line, :].max() - array[line, :].min())


def create_X(nb_lines, type, path, path_csv, nb):
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

    X = np.zeros(50 * nb_lines).reshape(50, nb_lines)

    number_data = [4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                   33,
                   34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]

    nb_line = -1

    with open(path_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            if nb_line >= 0:
                for i, index in enumerate(number_data):
                    X[i][nb_line] = float(row[index])
                X[len(number_data)][nb_line] = float(products.index(row[3]))
                X[len(number_data) + 1][nb_line] = float(int(row[55]) % 366) / 366.0

            nb_line += 1
        for i in range(49):
            normalize(X, i)
    np.save(path + 'X_' + type + '_' + str(nb) + '.npy', X)