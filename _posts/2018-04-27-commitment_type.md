---
layout: post
title: 'Emissions Reduction Commitments by Type'
tags:
hero: https://upload.wikimedia.org/wikipedia/commons/6/62/Smoke_of_chimneys_is_the_breath_of_Soviet_Russia.jpg
overlay: blue
published: true
---

At the conclusion of the UNFCCC's 21st Conference of Parties (COP) in Paris, each member nation submitted a report specifying the policy steps they intended to take to reduce greenhouse gas emission. These reports - known as Nationally Determined Commitments (NDC's) - and the emissions reduction strategies they incorporated were informed by the diverse economic and political situations felt by each nation. In order to make sense of these divergent strategies, I roughly classified the NDC's into three groups (Historical, Business as Usual & Other) and extracted essential information regarding emissions when sufficient information was available in the state's commitment report. 

The first [<font color='#4286f4'>map</font>](https://etoole.github.io/GIS_Final/commitment_type) is intended to easily convey the type of emission reduction strategy adopted by each country by color-coding this variable. It also includes data on each country's present emissions, target emissions (whether taken directly from the report or estimated), and average annual change in emissions which will allow the target to be reached. 

[![](https://etoole.github.io/GIS_Final/assets/img/commitment_type.png)](https://etoole.github.io/GIS_Final/commitment_type "Paris Climate Accord - Nationally Determined Commitments by Type. Eric Toole, 2018")

Countries that were classified as having a "Historical" emissions reduction scheme calculated their target in relation to the actual emissions measured in a historical year. For example, the European Union committed as block to reducing each nation's emissions to 40% of those measured in 1990 by the target year 2030. A number of countries outside of the EU with political affinities to that group also took the same pledge (e.g. Ukraine, Iceland & Norway) or slightly altered the model (e.g. Belarus, Moldova & Kazakhstan). Because a reduction relative to a historical year implies that peak emissions have already been reached, this type of commitment was more frequently undertaken by industrialized countries with ample resources and current emissions levels that are already high relative to the size of their population. 

Countries that are still undergoing the processes of industrialization and economic modernization have typically opted for what is called the "Business as Usual" (BAU) approach. Members of this group recognize the direct relationship between their economic development goals and increased greenhouse gas emissions. They also frequently make the point that their overall contribution to carbon dioxide levels has been minimal and that the contemporary emissions reduction imperative is the byproduct of the richest countries long history of burning fossil fuels with abandon. Therefor, emissions reductions are calculated relative to a baseline that is an estimate of future emissions if the country were to carry on doing "business as usual" rather than an actual measurement from a historical year. 

Details on the future emissions estimates are not always provided in full in the NDC's. Not all of the countries in this group even quantify their future baseline emissions. Some provide a baseline emissions amount but only give scant information on their methodology. Others are quite thorough and convincing. While standardized formulae for calculating future emissions were created by the UNFCCC, they were only occasionally cited. 

On the whole, commiting to reductions relative to a fictitious baseline widens the gap between reduction figures and reality. The use of incomensurable and occassionally opaque methodologies complicates the comparison of one BAU country's reduction goals to that of another. In addition, there is a built-in incentive to inflate these projections. For these reasons I independently recalculated the "business as usual" projections and the amount of emissions estimated for the target year using a uniform (if crude) method. Using a [<font color='#4286f4'>dataset obtained from the WorldBank</font>](https://github.com/etoole/GIS_Final/blob/master/data/Emissions_1995_to_2016.csv) that contained emissions measurements from 1995-2015, I wrote a small [<font color='#4286f4'>program</font>](https://github.com/etoole/GIS_Final/blob/master/calculate_ndc_amount.py) in the Python scripting language to carryout the following method. First, the percent change in emissions between each concurrent available year were calculated and placed in a list (e.g. [+2%, +4%, +1.8%, +0.2%]). These year-to-year emissions changes were then averaged to approximate the general emissions trend for each country over the 20 year period (e.g. +4%/year). The number of years between the year the NDC was signed and the target year was then calculated (e.g. 2025 - 2015 = 10) and the average change for the measured period was then compounded for the appropriate number of intervening years and multiplied by the emissions recorded for the year that nation signed its NDC (e.g. (1.04^<sup>10 = 1.48024428492</sup>) * 18.2 MTco2 = 26.94 MTco2). These "business as usual" emissions were then reduced by the specified amount to arrive at the emissions target (e.g. 26.94 MTco2 * (0.8 = 1 - 0.20) = 21.55 MTco2). 

To recap:

<p>
<font color='#75093b' size='3em' font-style='italicized' font-family='Courier New'>
emissions change list = [(1996 emissions / 1995 emissions) -1, (1997 emissions - 1996 emission) -1 * 100, etc.]
average emissions change = ((change1 + change2, etc.) / (number of changes in list)) + 1
bau emissions = ndc year emissions * (average emissions change^(bau target year - ndc year))
</font>
</p>


Given more time, a method that better accounts for anomolous factors would have been developed. For example, all members of the Former Soviet Union (FSU) experienced an abrupt reduction of emissions accompanying the economic contraction that followed the collapse of the Soviet Union. FSU states that opted for a BAU-type commitment (Georgia, Kyrgyzstan & Uzbekistan) could potentially have artificially low projections because of a rapid reduction trend which ceased two decades ago. Countries that have recently experienced rapid economic growth would also exhibit emissions trend volatility which would not be adequately captured by my method. The same could also be said for countries that experienced a period of turmoil that resulted in a temporary emissions slump.

Finally, members of the "Other" group focused on reforms that indirectly impacted greenhouse gas emissions rather than establishing a concrete emissions target. Many of the countries that fell into this third group were least developed nations with some of the lowest carbon intensive economies (co2/GDP/capita) and few resources to allocate towards government initiatives. These countries tended to favor low-cost initiatives such as reforestation, adopting new land use policies, and household-scale solar electrification in rural areas. 

This "Other" class also contains a group of five countries (China, Malaysia, Israel, Chile & Uruguay) which decided to gauge their reductions in terms of either an economic (co2/GDP unit) or demographic (tons co2/capita) carbon intensity metric rather than emissions amount. In order to fit these countries into my analysis framework, it would also be necessary to estimate their economic or demographic growth over the next 10 to 15 years. Such things are very difficult to predict. As well, whatever error was made in that initial estimate would be exaggerated by the subsequent calculations. I decided not to try and approximate their annual emissions change to reach the target because of the complexity and inaccuracy inherent to these projections. In a few cases, I was still able to interpolate others' translations of the intensity-based metrics into target emissions. In the case of China, a hugely significant player in the climate accord, I was able to find a range of potential target emissions based on Int'l Energy Agency (IEA) GDP growth projections on [<font color='#4286f4'>climateactiontracker.org</font>](http://climateactiontracker.org/countries/china/).

The last group is the "No Commitment Made". I was unable to find a PDF of their NDC in the UNFCCC-maintained repository, nor could I find anything alluding to emissions reduction goals or mitigation strategies. 

The second [<font color='#4286f4'>map</font>](https://etoole.github.io/GIS_Final/estimated_emissions) focuses on the annual change in emissions necessary for each nation to attain their emissions targets and uses the year that their NDC was signed as a starting point. Hot colors of increasing intensity are used to color countries with emissions targets that are above their recorded emissions in the year that their NDC was signed (a net increase). Greens of increasing darkness are used to color countries that plan to achieve a net reduction in their emissions from the year their NDC was signed to the target year described in the commitment.

[![](https://etoole.github.io/GIS_Final/assets/img/estimated_emissions.png)](https://etoole.github.io/GIS_Final/estimated_emissions "Paris Climate Accord - Annual Change in Emissions to reach Target. Eric Toole, 2018")

Once an target emission were estimated for each of the BAU countries, I was able to apply an inverted copound interest fomula to all of the countries which adopted Historical and BAU type commitments in order to calculate the average annual emissions change which would allow them to reach their target. This formula was included in the same Python script that was used to estimate the BAU emissions amounts. The first step was to compare the target emissions to the emissions measured for the year that each country's NDC was signed and to determine their proportion (e.g. 21.55 MTco2 / 18.2 MTco2 = 1.18406593407). This number represents the percentage change which will occur over all the years between the signing of the NDC and the target. Next, this proportion is exponentiated by the inversion of the difference between the target year and the NDC year (e.g. 1.18406593407^<sup>(1/(2025-2015))</sup>). By using an inverted exponent, the result takens into account the compounding of a constant percentage increase or decrease. It therefor assumes that this annual rate of change will be repeated each year until the target year.

Here is the formula: 

<p>
<font color='#75093b' size='3em' font-style='italicized' font-family='Courier New'>
(((target emissions / ndc year emissions)^<sup>(1 / years between ndc and target)</sup> - 1) * 100 = annual %change

(((21.55 MTco2 / 18.2 MTco2)^<sup>(1 / (2025 - 2015))</sup> - 1) * 100 = +1.70%/year
</font>
</p>

If you are interested in further reading, links for almost all of the actual NDC documents can be found in this [<font color='#4286f4'>csv file</font>](https://github.com/etoole/GIS_Final/blob/master/data/NDCs_details_calculated_with_avg_figures). 
