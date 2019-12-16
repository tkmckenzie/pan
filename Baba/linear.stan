data{
	int<lower=1> N;
	int<lower=1> k;
	
	matrix[N, k] X;
	vector[N] y;
	
	vector<lower=0>[k] beta_prior_sd;
	real<lower=0> sigma_prior_scale;
}
parameters{
	vector[k] beta;
	real<lower=0> sigma;
}
model{
	beta ~ normal(0, beta_prior_sd);
	sigma ~ cauchy(0, sigma_prior_scale);
	
	y ~ normal(X * beta, sigma);
}
