data {
    int<lower=0> N;
    vector[N] x1;
    vector[N] x2;
    vector[N] y;
}
parameters {
    real b1;
    real b2;
    real b3;
    real<lower=0> sigma;
}
transformed parameters {
    vector[N] mu;
    mu = b1 + b2 *x1 + b3*x2;
}
model {

    y ~ normal(mu, sigma);
}
