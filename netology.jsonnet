local k = (import 'ksonnet-util/kausal.libsonnet');
//by Ilya Zorin
{
  _config:: {
    name: 'change_me',
    namespace: std.extVar('qbec.io/defaultNs'),

    container: {
      requests: { cpu: '10m', memory: '100Mi' },
      limits: { cpu: '200m', memory: '200Mi' },
    },
  },

  local serviceAccount = k.core.v1.serviceAccount,

  serviceAccount:
    serviceAccount.new($._config.name) +
    serviceAccount.mixin.metadata.withNamespace($._config.namespace),
}
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
