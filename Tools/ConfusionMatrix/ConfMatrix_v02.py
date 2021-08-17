# Confusion Matrix

def ConfMatrix(TP, FP, FN, TN, **kwargs):

    # Source: https://en.wikipedia.org/wiki/Confusion_matrix
    # Important: Any change, change it in Prject 46 and after copy for use
    

    #                   Predicted
    #                   True   False
    # Observed   TRUE   TP     FP
    #           FALSE   FN     TN


    # ** kwargs ---------------------------------------------------------------

    # FNR =  Miss Rate
    # NPV =  Negative Predictive
    # FPR =  Fall-Out
    # FDR =  False Discovery
    # FOR =  False Omission
    # CSI =  Critical Success Index
    # MCC =  Matthews Correlation Coef.
    # BA =  Balanced Accuracy
    # PT =  Prevalence Threshold
    # FM =  Fowlkes-Mallows Index
    # BM =  Bookmaker Informedness
    # MK =  Markedness

    # decimals = Round to the given number of decimals. Default = 5



    # Main Program ------------------------------------------------------------

    round_size = 5

    Change_Decimals = kwargs.get("decimals")

    if Change_Decimals:

        round_size = Change_Decimals
      

    # Main Indexes (Always Calculated)

    TPR = round(TP/(TP+FN), round_size)     
    TNR = round(TN/(TN+FP), round_size)
    PPV = round(TP/(TP+FP), round_size)
    ACC = round((TP+TN)/(TP+TN+FP+FN), round_size)
    F1S = round(((2*TP)/(2*TP+FP+FN)), round_size)

    print("")
    print(f" > TPR =  Sensitivity  = {TPR}")
    print(f" > TNR =  Specificity  = {TNR}")
    print(f" > PPV =  Precision    = {PPV}")
    print(f" > ACC =  Accuracy     = {ACC}")
    print(f" > F1  =  F1 Score     = {F1S}")
    print("")


    # Optional Calculation (Called by kwargs) ---------------------------------
    
    Calc_FNR = kwargs.get("FNR")
    if(Calc_FNR == True):

        FNR = round(FN/(FN+TP), round_size)
        print(f" >> FNR =  Miss Rate  = {FNR}")


    Calc_NPV = kwargs.get("NPV")
    if(Calc_NPV == True):

        NPV = round(TN/(TN+FN), round_size)
        print(f" >> NPV =  Negative Predictive  = {NPV}")


    Calc_FPR = kwargs.get("FPR")
    if(Calc_FPR == True):

        FPR = round(FP/(FP+TN), round_size)
        print(f" >> FPR =  Fall-Out  = {FPR}")


    Calc_FDR = kwargs.get("FDR")
    if(Calc_FDR == True):

        FDR = round(FP/(FP+TP), round_size)
        print(f" >> FDR =  False Discovery  = {FDR}")


    Calc_FOR = kwargs.get("FOR")
    if(Calc_FOR == True):

        FOR = round(FN/(FN+TN), round_size)
        print(f" >> FOR =  False Omission  = {FOR}")


    Calc_CSI = kwargs.get("CSI")
    if(Calc_CSI == True):

        CSI  = round(TP/(TP+FN+FP), round_size)
        print(f" >> CSI =  Critical Success Index  = {CSI}")


    Calc_MCC = kwargs.get("MCC")
    if(Calc_MCC == True):

        MCC = (TP*TN - FP*FN)/((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))**(1/2)
        MCC = round(MCC, round_size)
        print(f" >> MCC =  Matthews Correlation Coef.  = {MCC}")


    Calc_BA = kwargs.get("BA")
    if(Calc_BA == True):

        BA  = round((TPR+TNR)/2, round_size)
        print(f" >> BA =  Balanced Accuracy  = {BA}")


    Calc_PT = kwargs.get("PT")
    if(Calc_PT == True):

        PT = ((TPR*((-1)*TNR+1))**(1/2)+TNR+1)/(TPR+TNR-1)
        PT = round(PT, round_size)
        print(f" >> PT =  Prevalence Threshold  = {PT}")
        

    Calc_FM = kwargs.get("FM")
    if(Calc_FM == True):

        FM = ((TP/(TP+FP))*(TP/(TP+FN)))**(1/2)
        FM = round(FM, round_size)
        print(f" >> FM =  Fowlkes-Mallows Index  = {FM}")


    Calc_BM = kwargs.get("BM")
    if(Calc_BM == True):

        BM = round(TPR+TNR-1, round_size)
        print(f" >> BM =  Bookmaker Informedness  = {BM}")


    Calc_MK = kwargs.get("MK")
    if(Calc_MK == True):

        MK = round(PPV+(TN/(TN+FN))-1, round_size)
        print(f" >> MK =  Markedness  = {MK}")



    # End ---------------------------------------------------------------------
    
    print("")

    
