#German Tax Benefit Calculator Static 2017


#German Tax Benefit Calculator

import pandas as pd 

def postgov_by_hours(pid, hours_1, hours_2):
    i = MASEdata_2017.index[MASEdata_2017["pid"]==pid].tolist()[0] #find index of pid
    pid = MASEdata_2017["pid"][i]
 
    num_of_children= MASEdata_2017["num_of_children"][i]
    n_child_0_1= MASEdata_2017["n_child_0_1"][i]
    n_child_2_4= MASEdata_2017["n_child_2_4"][i]
    n_child_5_7= MASEdata_2017["n_child_5_7"][i]
    n_child_8_10= MASEdata_2017["n_child_8_10"][i]
    n_child_11_12= MASEdata_2017["n_child_11_12"][i]
    n_child_13_15= MASEdata_2017["n_child_13_15"][i]
    n_child_16_18= MASEdata_2017["n_child_16_18"][i]
    private_transfers=MASEdata_2017["private_transfers"][i]
    Alg1= MASEdata_2017["ALG1"][i]
    unemployed_months= MASEdata_2017["unemployed_months"][i]
    employment_status= MASEdata_2017["employment_status"][i]
    annual_wages= MASEdata_2017["annual_wages"][i]
    labor_income_1= float(MASEdata_2017["labor_income"][i])
    if labor_income_1 != labor_income_1:
        labor_income_1 = 0 #!
    age= MASEdata_2017["age"][i]
    
    Alg2= MASEdata_2017["ALG2"][i]
    partner= MASEdata_2017["partner"][i]
    gender= MASEdata_2017["gender"][i]
    maternity_months= MASEdata_2017["maternity_months"][i]
    part_time_experince= MASEdata_2017["part_time_experience"][i]
    full_time_experince= MASEdata_2017["full_time_experience"][i]
    part_time_months= MASEdata_2017["part_time_months"][i]
    hb= MASEdata_2017["hb"][i]
    rent= MASEdata_2017["rent"][i]
    elderly_sa= MASEdata_2017["elderly_sa"][i]
    social_assistance_1= MASEdata_2017["social_assistance"][i]
    if  social_assistance_1 != social_assistance_1:
        social_assistance_1 = 0
    asset_income= MASEdata_2017["asset_income"][i]
    if asset_income != asset_income:
        asset_income = 0
    state= MASEdata_2017["state"][i]
    employment_level= MASEdata_2017["employment_level"][i]
    employment_status_now= MASEdata_2017["employment_status_now"][i]
    post_transfer_income=MASEdata_2017["post_gov_income"][i]
    syear=MASEdata_2017["syear"][i]
    income_last_year_1=MASEdata_2017["income_last_year_1"][i]
    if income_last_year_1 != income_last_year_1:
        income_last_year_1 = 0   
    wage_1=MASEdata_2017["wages"][i]/4
    if wage_1 != wage_1:
        wage_1 = 0
    working=MASEdata_2017["working"][i]
    log_wages=MASEdata_2017["log_wages"][i]
    
    age=MASEdata_2017["age"][i]
    unemployed_time=MASEdata_2017["unemployed_time"][i]
    partner_in_house=MASEdata_2017["partner_in_house"][i]
    partner_number=MASEdata_2017["partner_number"][i]
    work_experience=MASEdata_2017["work_experience"][i]
    hid=MASEdata_2017["hid"][i]
    disabled_1= MASEdata_2017["disabled_1"][i]

    if partner>=1 and partner<=4:
        partner=1
    else:
        partner=0

    num_hh_members= 1+partner+num_of_children 
    
   
    if partner==1:
        partner_index=MASEdata_2017.index[MASEdata_2017["pid"]==partner_number].tolist()
        if len(partner_index) != 0:
            partner_index = partner_index[0]
            income_last_year_2=MASEdata_2017["income_last_year_1"][partner_index]
            if  income_last_year_2 != income_last_year_2:
                income_last_year_2 = 0                       
            labor_income_2= float(MASEdata_2017["labor_income"][partner_index])
            if labor_income_2 != labor_income_2:
                labor_income_2 = 0  
            wage_2=MASEdata_2017["wages"][partner_index]/4
            if wage_2 != wage_2:
                wage_2 = 0
            social_assistance_2= MASEdata_2017["social_assistance"][partner_index]
            if social_assistance_2 != social_assistance_2:
                social_assistance_2 = 0
            disabled_2= MASEdata_2017["disabled_1"][partner_index]
            seen.add(partner_number)



    months = 12
    weeks = 52
    gov_index=1

    #Child Benefits
    child_benefit1= 192 #benefit amount for the first two children
    child_benefit2= 198 #third children
    child_benefit3= 223 #rest


    if num_of_children<=2:
        child_benefit_hh= num_of_children* months* child_benefit1
    elif num_of_children==3:
        child_benefit_hh= (2*months*child_benefit1)+(1*months*child_benefit2)
    else:
        child_benefit_hh= (2*months*child_benefit1)+(1*months*child_benefit2)+((num_of_children-3)*months*child_benefit3)


    #Social Security Contributions

    h_i =   0.073 # health insurance 
    l_i=    0.01525 #long term care insurance
    p_i =   0.093 #pension insurance
    u_i =   0.012 # unemployment insurance 

    ssch=4350 #monthly assessment ceiling for health insurance
    sscl=4350 #monthly assessment ceiling for long-term care insurance
    sscp=6350 #monthly assessment ceiling for pension insurance 
    sscu=6350 #monthly assessment ceiling for unemployment insurance
   

    if partner==0:
        health_contributions= h_i*min(labor_income_1, ssch)
        longterm_contributions= l_i*min(labor_income_1, sscl)
        pension_contributions= p_i*min(labor_income_1, sscp)
        unemp_contributions= u_i*min(labor_income_1, sscu)    
        ssc_hh = (health_contributions + longterm_contributions + pension_contributions + unemp_contributions)*months
    elif partner==1:
        health_contributions= h_i*min(labor_income_1, ssch) + h_i*min(labor_income_2, ssch)
        longterm_contributions= l_i*min(labor_income_1, sscl) + l_i*min(labor_income_2, sscl)
        pension_contributions= p_i*min(labor_income_1, sscp) + p_i*min(labor_income_2, sscp)
        unemp_contributions= u_i*min(labor_income_1, sscu) + u_i*min(labor_income_2, sscu)  
        ssc_hh = (health_contributions + longterm_contributions + pension_contributions + unemp_contributions)*months

    if partner==0:
        social_assistance_hh=social_assistance_1
    elif partner==1:
        social_assistance_hh=social_assistance_1+social_assistance_2



    #Arbeitslosengeld's (Unemployment Benefit 1)
    
    if partner==0:
        if wage_1*hours_1==0 and social_assistance_1==0:
            if income_last_year_1>0:
                if num_of_children>0:
                    ALG1_hh = min(0.67*income_last_year_1,6350)*months
                else:
                    ALG1_hh = min(0.60*income_last_year_1,6350)*months
            else:
                ALG1_hh=0
        else:
            ALG1_hh=0
    elif partner==1:
        if(wage_1*hours_1==0 and social_assistance_1==0)and(wage_2*hours_2>0):
            if income_last_year_1==0:
                ALG1_hh=0
            else:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_1, 6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_1, 6350)*months
        elif (wage_1*hours_1>0)and(wage_2*hours_2==0 and social_assistance_2==0):
            if income_last_year_2==0:
                ALG1_hh=0
            else:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months
        elif (wage_1*hours_1==0)and(wage_2*hours_2==0)and(social_assistance_hh==0):
            if income_last_year_1+income_last_year_2==0:
                ALG1_hh=0
            elif income_last_year_1>0:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months
            elif income_last_year_2>0:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months
            elif income_last_year_1>0 and income_last_year_2>0:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_1,6350)*months+min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months+min(0.60*income_last_year_1, 6350)*months
            else:
                ALG1_hh=0
        else:
            ALG1_hh=0           


    #Tax Formula
    #the following formula determines the tax liability for German tax payers

    if partner==0:
        taxable_income= child_benefit_hh+ ALG1_hh+ (wage_1*hours_1)*weeks - ssc_hh + asset_income #!
    elif partner==1:
        taxable_income= (child_benefit_hh+ ALG1_hh+ (wage_1* hours_1)*weeks+ (wage_2*hours_2)*months- ssc_hh +asset_income)/2 #assumed joint taxation of the income of the spouses #!

    if taxable_income<=8820:
        tax_liability=0
    elif (taxable_income>8820)& (taxable_income<=13769):
        tax_liability= (1007.27*((taxable_income-8652)/10000)+1400)*((taxable_income-8652)/10000)
    elif (taxable_income>13769)& (taxable_income<=54057):
        tax_liability= (223.76*((taxable_income-13669)/10000)+2397)*((taxable_income-13669)/10000)+939.57
    elif (taxable_income>54057)& (taxable_income<=256303):
        tax_liability = 0.42 * taxable_income - 8475.44
    else:
        tax_liability = 0.45 * taxable_income - 16164.53

    if partner==1:
        tax_liability=tax_liability*2

    #Solidarity surcharge (Solidaritätszuschlag)

    solidarity = min(0.055*tax_liability, max(0.119*(tax_liability-16596),0))


    if partner == 1:
        post_tax_income= 2*taxable_income-tax_liability-solidarity  #!
    else:
        post_tax_income= taxable_income-tax_liability-solidarity  #!


    #Social Assistance (Sozialhilfe) and ALG2 (Arbeitslosengeld II)
    if partner==0:
        if (num_of_children==0):
            benefit_amount_hh= 409+364.5+61
        elif (num_of_children==1):
            benefit_amount_hh= 409+437.4+73.2
        elif (num_of_children==2):
            benefit_amount_hh= 409+518.25+91.5
        elif (num_of_children==3):
            benefit_amount_hh= 409+587.35+103.7
        elif (num_of_children==4):
            benefit_amount_hh= 409+679.97+118.34
        elif (num_of_children>4):
            benefit_amount_hh=409+679.97+84.12*(num_of_children-4)+118.34+14.64*(num_of_children-4)
    elif partner==1:
        if (num_of_children==0):
            benefit_amount_hh= 368*2+437.4+73.2
        elif (num_of_children==1):
            benefit_amount_hh= 368*2+518.25+91.5
        elif (num_of_children==2):
            benefit_amount_hh= 368*2+587.35+103.7
        elif (num_of_children==3):
            benefit_amount_hh= 368*2+679.97+118.34
        elif (num_of_children>3):
            benefit_amount_hh=368*2+679.97+84.12*(num_of_children-3)+118.34+14.64*(num_of_children-3)
        
            
    benefit_amount_hh+=237*(n_child_0_1 + n_child_2_4 + 1/3 *n_child_5_7)+ 291*(2/3* n_child_5_7 + n_child_8_10 + n_child_11_12)+311*(n_child_13_15 + 1/3*n_child_16_18)+ 2/3*n_child_16_18*327

    

    unemp_income_allowance = 0
    post_tax_income /= months #!
    if post_tax_income<100:
        unemp_income_allowance = post_tax_income
    elif post_tax_income<1000:
        unemp_income_allowance = 0.2 * post_tax_income
    else:
        if (num_of_children>0) & (post_tax_income<1500):
            unemp_income_allowance = 0.1 * post_tax_income
        elif (num_of_children==0) & (post_tax_income<1200):
            unemp_income_allowance = 0.1 * post_tax_income

    unemp_wealth_allowance = 10050+partner*10050+ num_of_children*3100

    if asset_income<unemp_wealth_allowance:
        if benefit_amount_hh> post_tax_income- unemp_income_allowance:
            ALG2_hh = benefit_amount_hh - post_tax_income + unemp_income_allowance
        else:
            ALG2_hh=0
    else:
        ALG2_hh=0

    ALG2_hh *= months

    wealth_allowance_hh= 5000+ partner*5000+ num_of_children*500

    if partner==0:
        if (asset_income< wealth_allowance_hh)&(ALG2_hh==0)& (disabled_1==1):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        else: 
            sa_hh=0
    elif partner==1:
        if (asset_income< wealth_allowance_hh) & (disabled_1==1) & (disabled_2==1):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        elif (asset_income< wealth_allowance_hh) & (disabled_1==0) & (disabled_2==1):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        elif (asset_income< wealth_allowance_hh) & (disabled_1==1) & (disabled_2==0):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        else:
            sa_hh=0

    
    sa_hh *= months #!    


            

    #Housing Benefit(Wohngeld)

    #parameters of the rent burden function (parameters also exist for households with 7 to 12 members but not modelled here):
    if num_hh_members==1:
        a=4/100
        b=6.3/10000
        c=1.38/100000 
    elif num_hh_members==2:
        a=3/100
        b=4.4/10000
        c=1.03/100000
    elif num_hh_members==3:
        a=2/100
        b=3.8/10000
        c=8.3/100000
    elif num_hh_members==4:
        a=1/100
        b=3.4/10000
        c=4.3/100000   
    elif num_hh_members==5:
        a=0/100
        b=3/10000
        c=4.2/100000   
    elif num_hh_members==6:
        a=-1/100
        b=2.8/10000
        c=3.6/100000
        

    if ALG2_hh>0:
        hb_hh=0
    else:
        if (num_hh_members==1)& (post_tax_income<955):
            if rent<= 434:
                hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
            else:
                hb_hh=0
        elif (num_hh_members==2):
            if partner==0:
                if post_tax_income<1307:
                    if rent<= 526:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<1307:
                    if rent<=526:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==3):
            if partner==0:
                if post_tax_income<1585:
                    if rent<=626:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else: 
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<1585:
                    if rent<=626:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==4):
            if partner==0:
                if post_tax_income<2075:
                    if rent<=730:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<2075:
                    if rent<=730:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==5):
            if partner==0:
                if post_tax_income<2362:
                    if rent<=834:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<2362:
                    if rent<=834:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==6):
            if partner==0:
                if post_tax_income<2664:
                    if rent<=935:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<2664:
                    if rent<=935:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        else:
            hb_hh=0

    if hb_hh<10:
        hb_hh=0
    else:
        hb_hh=hb_hh

    job_choices = [0,10,20,30,40,50,60]
    post_tax_income *= months
    post_government_hh= post_tax_income+ALG2_hh+sa_hh+hb_hh+asset_income+private_transfers
    return post_government_hh


MASEdata_2017 = pd.read_stata("MASEdata2017.dta")
results2017= []
results2017.append(["syear","pid","partner","hid","dpi"])

seen= set()

for i in range(MASEdata_2017.shape[0]):
    pid = MASEdata_2017["pid"][i]
    if pid in seen:
        continue
    else:
        seen.add(pid)
    num_of_children= MASEdata_2017["num_of_children"][i]
    n_child_0_1= MASEdata_2017["n_child_0_1"][i]
    n_child_2_4= MASEdata_2017["n_child_2_4"][i]
    n_child_5_7= MASEdata_2017["n_child_5_7"][i]
    n_child_8_10= MASEdata_2017["n_child_8_10"][i]
    n_child_11_12= MASEdata_2017["n_child_11_12"][i]
    n_child_13_15= MASEdata_2017["n_child_13_15"][i]
    n_child_16_18= MASEdata_2017["n_child_16_18"][i]
    Alg1= MASEdata_2017["ALG1"][i]
    unemployed_months= MASEdata_2017["unemployed_months"][i]
    employment_status= MASEdata_2017["employment_status"][i]
    annual_wages= MASEdata_2017["annual_wages"][i]
    labor_income_1= float(MASEdata_2017["labor_income"][i])
    if labor_income_1 != labor_income_1:
        labor_income_1 = 0
    age= MASEdata_2017["age"][i]
    #worktime_weekly= MASEdata_2017["worktime_weekly"][i]
    private_transfers=MASEdata_2017["private_transfers"][i]
    Alg2= MASEdata_2017["ALG2"][i]
    partner= MASEdata_2017["partner"][i]
    gender= MASEdata_2017["gender"][i]
    maternity_months= MASEdata_2017["maternity_months"][i]
    part_time_experince= MASEdata_2017["part_time_experience"][i]
    full_time_experince= MASEdata_2017["full_time_experience"][i]
    part_time_months= MASEdata_2017["part_time_months"][i]
    hb= MASEdata_2017["hb"][i]
    rent= MASEdata_2017["rent"][i]
    elderly_sa= MASEdata_2017["elderly_sa"][i]
    social_assistance_1= MASEdata_2017["social_assistance"][i]
    if social_assistance_1 != social_assistance_1:
        social_assistance_1 = 0
    asset_income= MASEdata_2017["asset_income"][i]
    if asset_income != asset_income:
        asset_income = 0
    state= MASEdata_2017["state"][i]
    employment_level= MASEdata_2017["employment_level"][i]
    employment_status_now= MASEdata_2017["employment_status_now"][i]
    post_transfer_income=MASEdata_2017["post_gov_income"][i]
    syear=MASEdata_2017["syear"][i]
    income_last_year_1=MASEdata_2017["income_last_year_1"][i]
    if income_last_year_1 != income_last_year_1:
        income_last_year_1 = 0
    wage_1=MASEdata_2017["wages"][i]/4
    if  wage_1 != wage_1:
        wage_1 = 0
    working=MASEdata_2017["working"][i]
    log_wages=MASEdata_2017["log_wages"][i]
    hours_1=MASEdata_2017["hours"][i]
    if  hours_1 != hours_1:
        hours_1 = 0
    age=MASEdata_2017["age"][i]
    unemployed_time=MASEdata_2017["unemployed_time"][i]
    partner_in_house=MASEdata_2017["partner_in_house"][i]
    partner_number=MASEdata_2017["partner_number"][i]
    work_experience=MASEdata_2017["work_experience"][i]
    hid=MASEdata_2017["hid"][i]
    
    disabled_1= MASEdata_2017["disabled_1"][i]

    if partner>=1 and partner<=4:
        partner=1
    else:
        partner=0

    num_hh_members= 1+partner+num_of_children 
    
   
    if partner==1:
        partner_index=MASEdata_2017.index[MASEdata_2017["pid"]==partner_number].tolist()
        if len(partner_index) != 0:
            partner_index = partner_index[0]
            income_last_year_2=MASEdata_2017["income_last_year_1"][partner_index]
            if  income_last_year_2 != income_last_year_2:
                income_last_year_2 = 0
            labor_income_2= float(MASEdata_2017["labor_income"][partner_index])
            if  labor_income_2 != labor_income_2:
                labor_income_2 = 0
            hours_2=MASEdata_2017["hours"][partner_index]
            if  hours_2 != hours_2:
                hours_2 = 0
            wage_2=MASEdata_2017["wages"][partner_index]/4
            if  wage_2 != wage_2:
                wage_2 = 0
            social_assistance_2= MASEdata_2017["social_assistance"][partner_index]
            if  social_assistance_2 != social_assistance_2:
                social_assistance_2 = 0
            disabled_2= MASEdata_2017["disabled_1"][partner_index]
            seen.add(partner_number)
        else:
            continue

        
    


    months = 12
    weeks = 52
    gov_index=1

    #Child Benefits
    child_benefit1= 192 #benefit amount for the first two children
    child_benefit2= 198 #third children
    child_benefit3= 223 #rest

    if num_of_children<=2:
        child_benefit_hh= num_of_children* months* child_benefit1
    elif num_of_children==3:
        child_benefit_hh= (2*months*child_benefit1)+(1*months*child_benefit2)
    else:
        child_benefit_hh= (2*months*child_benefit1)+(1*months*child_benefit2)+((num_of_children-3)*months*child_benefit3)


    #Social Security Contributions

    h_i =   0.073 # health insurance 
    l_i=    0.01525 #long term care insurance
    p_i =   0.093 #pension insurance
    u_i =   0.012 # unemployment insurance 


    ssch=4350 #monthly assessment ceiling for health insurance
    sscl=4350 #monthly assessment ceiling for long-term care insurance
    sscp=6350 #monthly assessment ceiling for pension insurance 
    sscu=6350 #monthly assessment ceiling for unemployment insurance

    if partner==0:
        health_contributions= h_i*min(labor_income_1, ssch)
        longterm_contributions= l_i*min(labor_income_1, sscl)
        pension_contributions= p_i*min(labor_income_1, sscp)
        unemp_contributions= u_i*min(labor_income_1, sscu)    
        ssc_hh = (health_contributions + longterm_contributions + pension_contributions + unemp_contributions)*months
    elif partner==1:
        health_contributions= h_i*min(labor_income_1, ssch) + h_i*min(labor_income_2, ssch)
        longterm_contributions= l_i*min(labor_income_1, sscl) + l_i*min(labor_income_2, sscl)
        pension_contributions= p_i*min(labor_income_1, sscp) + p_i*min(labor_income_2, sscp)
        unemp_contributions= u_i*min(labor_income_1, sscu) + u_i*min(labor_income_2, sscu)  
        ssc_hh = (health_contributions + longterm_contributions + pension_contributions + unemp_contributions)*months

    if partner==0:
        social_assistance_hh=social_assistance_1
    elif partner==1:
        social_assistance_hh=social_assistance_1+social_assistance_2



    #Arbeitslosengeld's (Unemployment Benefit 1)
    
    if partner==0:
        if wage_1*hours_1==0 and social_assistance_1==0:
            if income_last_year_1>0:
                if num_of_children>0:
                    ALG1_hh = min(0.67*income_last_year_1,6350)*months
                else:
                    ALG1_hh = min(0.60*income_last_year_1,6350)*months
            else:
                ALG1_hh=0
        else:
            ALG1_hh=0
    elif partner==1:
        if(wage_1*hours_1==0 and social_assistance_1==0)and(wage_2*hours_2>0):
            if income_last_year_1==0:
                ALG1_hh=0
            else:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_1, 6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_1, 6350)*months
        elif (wage_1*hours_1>0)and(wage_2*hours_2==0 and social_assistance_2==0):
            if income_last_year_2==0:
                ALG1_hh=0
            else:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months
        elif (wage_1*hours_1==0)and(wage_2*hours_2==0)and(social_assistance_hh==0):
            if income_last_year_1+income_last_year_2==0:
                ALG1_hh=0
            elif income_last_year_1>0:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months
            elif income_last_year_2>0:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months
            elif income_last_year_1>0 and income_last_year_2>0:
                if num_of_children>0:
                    ALG1_hh=min(0.67*income_last_year_1,6350)*months+min(0.67*income_last_year_2,6350)*months
                else:
                    ALG1_hh=min(0.60*income_last_year_2, 6350)*months+min(0.60*income_last_year_1, 6350)*months
            else:
                ALG1_hh=0
        else:
            ALG1_hh=0           

    #Tax Formula
    #the following formula determines the tax liability for German tax payers

    if partner==0:
        taxable_income= child_benefit_hh+ ALG1_hh+ (wage_1*hours_1)*weeks - ssc_hh + asset_income #!
    elif partner==1:
        taxable_income= (child_benefit_hh+ ALG1_hh+ (wage_1* hours_1)*weeks+ (wage_2*hours_2)*months- ssc_hh +asset_income)/2 #assumed joint taxation of the income of the spouses #!

    if taxable_income<=8820:
        tax_liability=0
    elif (taxable_income>8820)& (taxable_income<=13769):
        tax_liability= (1007.27*((taxable_income-8652)/10000)+1400)*((taxable_income-8652)/10000)
    elif (taxable_income>13769)& (taxable_income<=54057):
        tax_liability= (223.76*((taxable_income-13669)/10000)+2397)*((taxable_income-13669)/10000)+939.57
    elif (taxable_income>54057)& (taxable_income<=256303):
        tax_liability = 0.42 * taxable_income - 8475.44
    else:
        tax_liability = 0.45 * taxable_income - 16164.53

    if partner == 1:
        tax_liability = tax_liability*2
    #Solidarity surcharge (Solidaritätszuschlag)

    solidarity = min(0.055*tax_liability, max(0.119*(tax_liability-16596),0))


    if partner == 1: #!
        post_tax_income= 2* taxable_income-tax_liability-solidarity 
    else:
        post_tax_income= taxable_income-tax_liability-solidarity 

    #Social Assistance (Sozialhilfe) and ALG2 (Arbeitslosengeld II)
    if partner==0:
        if (num_of_children==0):
            benefit_amount_hh= 409+364.5+61
        elif (num_of_children==1):
            benefit_amount_hh= 409+437.4+73.2
        elif (num_of_children==2):
            benefit_amount_hh= 409+518.25+91.5
        elif (num_of_children==3):
            benefit_amount_hh= 409+587.35+103.7
        elif (num_of_children==4):
            benefit_amount_hh= 409+679.97+118.34
        elif (num_of_children>4):
            benefit_amount_hh=409+679.97+84.12*(num_of_children-4)+118.34+14.64*(num_of_children-4)
    elif partner==1:
        if (num_of_children==0):
            benefit_amount_hh= 368*2+437.4+73.2
        elif (num_of_children==1):
            benefit_amount_hh= 368*2+518.25+91.5
        elif (num_of_children==2):
            benefit_amount_hh= 368*2+587.35+103.7
        elif (num_of_children==3):
            benefit_amount_hh= 368*2+679.97+118.34
        elif (num_of_children>3):
            benefit_amount_hh=368*2+679.97+84.12*(num_of_children-3)+118.34+14.64*(num_of_children-3)
        
            
    benefit_amount_hh+=237*(n_child_0_1 + n_child_2_4 + 1/3 *n_child_5_7)+ 291*(2/3* n_child_5_7 + n_child_8_10 + n_child_11_12)+311*(n_child_13_15 + 1/3*n_child_16_18)+ 2/3*n_child_16_18*327

    


    unemp_income_allowance = 0
    post_tax_income /= months
    if post_tax_income<100:
        unemp_income_allowance = post_tax_income
    elif post_tax_income<1000:
        unemp_income_allowance = 0.2 * post_tax_income
    else:
        if (num_of_children>0) & (post_tax_income<1500):
            unemp_income_allowance = 0.1 * post_tax_income
        elif (num_of_children==0) & (post_tax_income<1200):
            unemp_income_allowance = 0.1 * post_tax_income

    unemp_wealth_allowance = 10050+partner*10050+ num_of_children*3100

    if asset_income<unemp_wealth_allowance:
        if benefit_amount_hh> post_tax_income- unemp_income_allowance:
            ALG2_hh = benefit_amount_hh - post_tax_income + unemp_income_allowance
        else:
            ALG2_hh=0
    else:
        ALG2_hh=0

    ALG2_hh *= months #!

    wealth_allowance_hh= 5000+ partner*5000+ num_of_children*500

    if partner==0:
        if (asset_income< wealth_allowance_hh)&(ALG2_hh==0)& (disabled_1==1):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        else: 
            sa_hh=0
    elif partner==1:
        if (asset_income< wealth_allowance_hh) & (disabled_1==1) & (disabled_2==1):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        elif (asset_income< wealth_allowance_hh) & (disabled_1==0) & (disabled_2==1):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        elif (asset_income< wealth_allowance_hh) & (disabled_1==1) & (disabled_2==0):
            income_allowance_hh=min(benefit_amount_hh/2, post_tax_income*3/10)
            if post_tax_income - income_allowance_hh < benefit_amount_hh:
                sa_hh= post_tax_income - income_allowance_hh
            else:
                sa_hh=0
        else:
            sa_hh=0


    sa_hh *= months #!        

    #Housing Benefit(Wohngeld)

    #parameters of the rent burden function (parameters also exist for households with 7 to 12 members but not modelled here):
    if num_hh_members==1:
        a=4/100
        b=6.3/10000
        c=1.38/100000 
    elif num_hh_members==2:
        a=3/100
        b=4.4/10000
        c=1.03/100000
    elif num_hh_members==3:
        a=2/100
        b=3.8/10000
        c=8.3/100000
    elif num_hh_members==4:
        a=1/100
        b=3.4/10000
        c=4.3/100000   
    elif num_hh_members==5:
        a=0/100
        b=3/10000
        c=4.2/100000   
    elif num_hh_members==6:
        a=-1/100
        b=2.8/10000
        c=3.6/100000
        

    if ALG2_hh>0:
        hb_hh=0
    else:
        if (num_hh_members==1)& (post_tax_income<955):
            if rent<= 434:
                hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
            else:
                hb_hh=0
        elif (num_hh_members==2):
            if partner==0:
                if post_tax_income<1307:
                    if rent<= 526:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<1307:
                    if rent<=526:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==3):
            if partner==0:
                if post_tax_income<1585:
                    if rent<=626:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else: 
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<1585:
                    if rent<=626:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==4):
            if partner==0:
                if post_tax_income<2075:
                    if rent<=730:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<2075:
                    if rent<=730:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==5):
            if partner==0:
                if post_tax_income<2362:
                    if rent<=834:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<2362:
                    if rent<=834:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        elif (num_hh_members==6):
            if partner==0:
                if post_tax_income<2664:
                    if rent<=935:
                        hb_hh= 1.15*(rent-(a+b*rent+c*post_tax_income)*post_tax_income)
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
            else:
                if post_tax_income<2664:
                    if rent<=935:
                        hb_hh= 1.15*(rent-(a+b*rent+c*(post_tax_income))*(post_tax_income))
                    else:
                        hb_hh=0
                else:
                    hb_hh=0
        else:
            hb_hh=0

    if hb_hh<10:
        hb_hh=0
    else:
        hb_hh=hb_hh

    post_tax_income *= months #!
    post_government_hh= post_tax_income+ALG2_hh+sa_hh+hb_hh+asset_income+private_transfers
    results2017.append([syear, pid, partner, hid, post_government_hh])


pdresults= pd.DataFrame(results2017)
pdresults.to_csv("results2017static.csv")