def plot_residuals(df, actual, resids):

    sns.scatterplot(data = df, x = actual, y = resids)

    plt.hlines(0, 0, df[actual].max())

    plt.show()
    
    
    
def regression_errors(df, actual, preds):
    
    SSE2 = mean_squared_error(df[actual], df[preds])*len(df)
    
    ESS = sum((df[preds] - df[actual].mean())**2)
    
    TSS = SSE2 + ESS
    
    MSE2 = mean_squared_error(df[actual], df[preds])
    
    RMSE2 = sqrt(mean_squared_error(df[actual], df[preds]))
    
    print(f'SSE2: {round(SSE2)}')
    print(f'ESS: {round(ESS)}')
    print(f'TSS: {round(TSS)}')
    print(f'MSE2: {round(MSE2)}')
    print(f'RMSE2: {round(RMSE2)}')
    
    
    
def baseline_errors(df, actual, baseline):
    
    SSE2_base = mean_squared_error(df[actual], df[baseline])*len(df)
    
    MSE2_base = mean_squared_error(df[actual], df[baseline])
    
    RMSE2_base = sqrt(mean_squared_error(df[actual], df[baseline]))
    
    print(f'SSE2_base: {round(SSE2_base)}')
    print(f'MSE2_base: {round(MSE2_base)}')
    print(f'RMSE2_base: {round(RMSE2_base)}')
    
    
    
def better_than_baseline(df, actual, baseline, preds):
    
    RMSE2_base = sqrt(mean_squared_error(df[actual], df[baseline]))
    
    RMSE2 = sqrt(mean_squared_error(df[actual], df[preds]))
    
    print(f'RMSE of our baseline: {round(RMSE2_base)}')
    print(f'RMSE of our finely tuned model: {round(RMSE2)}')
    print('')
    print('Model performs better than baseline?')
    
    return RMSE2 < RMSE2_base