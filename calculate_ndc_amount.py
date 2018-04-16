import csv

emissions_year_dict_list = []


with open('./data/NDCs_details.csv') as NDC_data:
    NDC_spreadsheet = csv.DictReader(NDC_data, delimiter='~')

    with open('./data/Emissions_1995_to_2016.csv') as emissions_data:
        emissions_spreadsheet = csv.DictReader(emissions_data)

        with open('./data/NDCs_details_calculated.csv', 'w') as output:
            fieldnames = ['Country','NDC Link','NDC Year','NDC Year Emissions','NDC Type','Emissions Type','Base Year','Base Year Emissions','Percent Reduction Min','Percent Reduction Max','Reduction Amount Min','Reduction Amount Max','Emissions Limit Min','Emissions Limit Max','Target Year','Target Average Annual Change Min','Target Average Annual Change Max','Conditional']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for emissions_row in emissions_spreadsheet:
                # print(emissions_row)
                # if emissions_row['Year'] == '2005':
                    # print(emissions_row['Azerbaijan'])
                emissions_year_dict_list.append(emissions_row)

            # print(emissions_year_dict_list)


            for commitment_row in NDC_spreadsheet:
                # print(commitment_row)
                country = ""
                ndc_year = ""
                ndc_link = ""
                ndc_type = ""
                emissions_type = ""
                base_year = ""
                base_year_emissions = ""
                percent_red_min = ""
                percent_red_max = ""
                red_amt_min =  ""
                red_amt_max =  ""
                emissions_limit_min = ""
                emissions_limit_max = ""
                target_year = ""
                conditional = ""
                target_annual_change_max = ""
                target_annual_change_min = ""

                country = commitment_row['Country']
                ndc_year = commitment_row['NDC Year']
                ndc_link = commitment_row['NDC Link']
                ndc_type = commitment_row['NDC Type']
                emissions_type = commitment_row['Emissions Type']
                base_year = commitment_row['Base Year']
                base_year_emissions = commitment_row['Base Year Emissions']
                percent_red_min = commitment_row['Percent Reduction Min']
                percent_red_max = commitment_row['Percent Reduction Max']
                red_amt_min = commitment_row['Reduction Amount Min']
                red_amt_max = commitment_row['Reduction Amount Max']
                emissions_limit_min = commitment_row['Emissions Limit Min']
                emissions_limit_max = commitment_row['Emissions Limit Max']
                target_year = commitment_row['Target Year']
                target_annual_change_max = commitment_row['Target Average Annual Change Max']
                target_annual_change_min = commitment_row['Target Average Annual Change Min']
                conditional = commitment_row['Conditional']
                # print(country)
                # print(ndc_year)
                # print(target_year)

                if ndc_year != "":
                    if target_year !="":
                        ndc_year_to_target = int(target_year) - int(ndc_year)
                        # print(ndc_year_to_target)
                # print(country)
                # print(ndc_type)
                if ndc_type == 'Historical':
                    # print(country)
                    for emissions_row in emissions_year_dict_list:
                        # print(country)
                        # print(base_year)
                        # print(emissions_row)

                        if emissions_row['Year'] == ndc_year:
                            ndc_year_emissions = round(float(emissions_row[country]), 3)
                            commitment_row['NDC Year Emissions'] = "{0} MTco2".format(ndc_year_emissions)
                            # print(ndc_year_emissions)
                        if emissions_row['Year'] == base_year:
                            base_year_emissions = round(float(emissions_row[country]), 3)
                            commitment_row['Base Year Emissions'] = "{0} MTco2".format(base_year_emissions)
                            # print(country)
                            # print(emissions_row[country])
                            # print(commitment_row)

                    # print(base_year_emissions)
                    emissions_limit_max = round(int(base_year_emissions) * (1 - (float(percent_red_min)/100)), 3)
                    commitment_row['Emissions Limit Max'] = "{0} MTco2".format(emissions_limit_max)
                    # print(emissions_limit_max)

                    red_amt_min = round(base_year_emissions - emissions_limit_max, 3)
                    commitment_row['Reduction Amount Min'] = "{0} MTco2".format(red_amt_min)
                    # print(red_amt_min)

                    target_annual_change_min = round(100 * (((emissions_limit_max/float(ndc_year_emissions)) ** (1/ndc_year_to_target)) - 1), 2)
                    commitment_row['Target Average Annual Change Min'] = "{0}%/year".format(target_annual_change_min)
                    # print(target_annual_change_min)

                    if percent_red_max != "":
                        emissions_limit_min = round(int(base_year_emissions) * (1 - (float(percent_red_max)/100)), 3)
                        commitment_row['Emissions Limit Min'] = "{0} MTco2".format(emissions_limit_min)
                        # print(emissions_limit_min)

                        red_amt_max = round(base_year_emissions - emissions_limit_min, 3)
                        commitment_row['Reduction Amount Max'] = "{0} MTco2".format(red_amt_max)
                        # print(red_amt_max)

                        target_annual_change_max = round(100 * (((emissions_limit_min/float(ndc_year_emissions)) ** (1/ndc_year_to_target)) - 1), 2)
                        commitment_row['Target Average Annual Change Max'] = "{0}%/year".format(target_annual_change_max)
                        # print(target_annual_change_max)







                elif ndc_type == "BAU":
                    historical_emissions_list = []
                    emissions_change_list = []
                    # print(country)
                    for emissions_row in emissions_year_dict_list:
                        # print(emissions_row[country])

                        if ndc_year != "":
                            if ndc_year != "2017":
                                if emissions_row['Year'] == ndc_year:
                                    ndc_year_emissions = emissions_row[country]
                                    ndc_year_emissions = round(float(ndc_year_emissions), 3)
                                    commitment_row['NDC Year Emissions'] = "{0} MTco2*".format(ndc_year_emissions)
                                    # print(ndc_year_emissions)

                        if emissions_row[country] != "":
                            historical_emissions_list.append(emissions_row[country])
                            last_year_recorded = emissions_row['Year']
                            last_emission_recorded = emissions_row[country]
                    # print(historical_emissions_list)
                    # print(len(historical_emissions_list))
                    i = -1
                    for annual_emission in historical_emissions_list:
                        i += 1
                        if i != (len(historical_emissions_list) - 1):
                            # print(i)
                            # print(annual_emission)
                            # print(historical_emissions_list[i + 1])
                            next_year_emission = float(historical_emissions_list[i+1])
                            annual_emission = float(annual_emission)
                            emissions_change = (next_year_emission/annual_emission) - 1
                            # print(emissions_change)
                            emissions_change_list.append(emissions_change)
                    # print(emissions_change_list)
                    # print(sum(emissions_change_list))
                    # print(len(emissions_change_list))
                    average_emissions_change = ((sum(emissions_change_list))/(len(emissions_change_list))) + 1
                    # print(average_emissions_change)

                    years_to_target = (int(target_year)) - int(last_year_recorded)
                    # print(years_to_target)
                    bau_extrapolation_percent = average_emissions_change ** years_to_target
                    # print(bau_extrapolation_percent)
                    # print(float(last_emission_recorded) * bau_extrapolation_percent)
                    bau_emission_target_year = round(float(last_emission_recorded) * bau_extrapolation_percent, 3)
                    # print(bau_emission_target_year)
                    # print(bau_emission_target_year)
                    # print(percent_red_min)
                    commitment_row['Base Year Emissions'] = "{0} MTco2*".format(bau_emission_target_year)

                    percent_red_min = (100 - float(percent_red_min))/100
                    emissions_target_amt_max_calculated = round(percent_red_min * bau_emission_target_year, 3)
                    # print(last_emission_recorded)
                    # print(emissions_target_amt_min_calculated)
                    commitment_row['Emissions Limit Max'] = "{0} MTco2*".format(emissions_target_amt_max_calculated)

                    reduction_amt_min_calculated = round(bau_emission_target_year - emissions_target_amt_max_calculated, 3)
                    commitment_row['Reduction Amount Min'] = "{0} MTco2*".format(reduction_amt_min_calculated)

                    target_annual_change_min = round(100 * (((emissions_target_amt_max_calculated/float(ndc_year_emissions)) ** (1/ndc_year_to_target)) - 1), 2)
                    commitment_row['Target Average Annual Change Min'] = "{0}%/year".format(target_annual_change_min)




                    if percent_red_max != "":
                        percent_red_max = (100 - float(percent_red_max))/100
                        emissions_target_amt_min_calculated = round(percent_red_max * bau_emission_target_year, 3)
                        commitment_row['Emissions Limit Min'] = "{0} MTco2*".format(emissions_target_amt_min_calculated)
                        reduction_amt_max_calculated = round(bau_emission_target_year - emissions_target_amt_min_calculated, 3)
                        commitment_row['Reduction Amount Max'] = "{0} MTco2*".format(reduction_amt_max_calculated)

                        target_annual_change_max = round(100 * (((emissions_target_amt_min_calculated/float(ndc_year_emissions)) ** (1/ndc_year_to_target)) -1), 2)
                        commitment_row['Target Average Annual Change Max'] = "{0}%/year".format(target_annual_change_max)
                        # print(ndc_year_to_target)
                        # print("minimum change proportion")
                        # print((emissions_target_amt_max_calculated/float(ndc_year_emissions)))
                        # print('minimum change rate')
                        # print(target_annual_change_min)
                        # print('max change proportion')
                        # print((emissions_target_amt_min_calculated/float(ndc_year_emissions)))
                        # print('max change rate')
                        # print(target_annual_change_max)

                #
                print(commitment_row)
                writer.writerow(commitment_row)
