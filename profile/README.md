<!-- Netcracker / .github / profile/README.md -->

<h1 align="center">Netcracker Open Source</h1>

<p align="center">
  <b>Qubership</b> — cloud-native building blocks for API governance, integration, observability and Kubernetes platforms
</p>

---

## 👋 About

Netcracker engineers build and open-source **Qubership** — a family of production-proven components that power our own cloud platforms: an API registry and developer portal, an integration platform on Apache Camel, the Cloud Core microservice framework and service mesh, a full observability stack, Kubernetes operators for data and messaging services, and the tooling to test, configure and deliver it all.

---

## 🗂 Product Domains

<table>
  <tr>
    <td valign="top" width="50%">
      <h3>🧩 APIHUB</h3>
      <p>API registry and developer portal: one place for OpenAPI, GraphQL and AsyncAPI specs, with versioning, breaking-change detection, linting and MCP access — in one monorepo.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-apihub">qubership-apihub</a> — the platform</li>
        <li>API registry — Go backend</li>
        <li>builder — spec processing &amp; diff pipeline</li>
        <li>web portal, API linter, in-cluster agents</li>
      </ul>
    </td>
    <td valign="top" width="50%">
      <h3>🔗 Cloud Integration Platform</h3>
      <p>Open-source integration and orchestration platform built on Apache Camel: visual flow designer, runtime engines, session tracing and testing — in one monorepo.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-integration-platform">qubership-integration-platform</a> — the platform</li>
        <li>engine &amp; micro-engine — Spring Boot / Quarkus runtimes</li>
        <li>runtime catalog &amp; sessions management</li>
        <li>web UI, VS Code extension, testing service</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <h3>☁️ Cloud Core &amp; Service Mesh</h3>
      <p>Foundation for microservices on Kubernetes: service mesh control plane and gateways, messaging- and database-as-a-service, Java and Go frameworks.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-core-control-plane">qubership-core-control-plane</a> — service mesh control plane</li>
        <li><a href="https://github.com/Netcracker/qubership-core-ingress-gateway">qubership-core-ingress-gateway</a> — Envoy-based gateway</li>
        <li><a href="https://github.com/Netcracker/qubership-maas">qubership-maas</a> · <a href="https://github.com/Netcracker/qubership-dbaas">qubership-dbaas</a> — messaging &amp; DB as a service</li>
        <li><a href="https://github.com/Netcracker/qubership-core-java-libs">qubership-core-java-libs</a> — Spring &amp; Quarkus libraries</li>
        <li><a href="https://github.com/Netcracker/qubership-core-lib-go">qubership-core-lib-go</a> — Go microservice utilities</li>
      </ul>
      <details>
        <summary><b>All 42 repositories</b></summary>
        <p><b>Platform services</b><br>
        <a href="https://github.com/Netcracker/qubership-core-control-plane">qubership-core-control-plane</a> · <a href="https://github.com/Netcracker/qubership-core-ingress-gateway">qubership-core-ingress-gateway</a> · <a href="https://github.com/Netcracker/qubership-core-site-management">qubership-core-site-management</a> · <a href="https://github.com/Netcracker/qubership-core-paas-mediation">qubership-core-paas-mediation</a> · <a href="https://github.com/Netcracker/qubership-core-config-server">qubership-core-config-server</a> · <a href="https://github.com/Netcracker/qubership-core-facade-operator">qubership-core-facade-operator</a> · <a href="https://github.com/Netcracker/qubership-core-core-operator">qubership-core-core-operator</a> · <a href="https://github.com/Netcracker/qubership-istio">qubership-istio</a> · <a href="https://github.com/Netcracker/qubership-core-mesh-config">qubership-core-mesh-config</a> · <a href="https://github.com/Netcracker/qubership-rate-limiter">qubership-rate-limiter</a> · <a href="https://github.com/Netcracker/qubership-mini-core">qubership-mini-core</a></p>
        <p><b>MaaS &amp; DBaaS</b><br>
        <a href="https://github.com/Netcracker/qubership-maas">qubership-maas</a> · <a href="https://github.com/Netcracker/qubership-core-maas-agent">qubership-core-maas-agent</a> · <a href="https://github.com/Netcracker/qubership-dbaas">qubership-dbaas</a> · <a href="https://github.com/Netcracker/qubership-core-dbaas-agent">qubership-core-dbaas-agent</a> · <a href="https://github.com/Netcracker/qubership-dbaas-adapter-core">qubership-dbaas-adapter-core</a></p>
        <p><b>Java libraries</b><br>
        <a href="https://github.com/Netcracker/qubership-core-java-libs">qubership-core-java-libs</a></p>
        <p><b>Go libraries</b> <sub><code>qubership-core-lib-go-*</code></sub><br>
        <a href="https://github.com/Netcracker/qubership-core-lib-go">qubership-core-lib-go</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-actuator-common">actuator-common</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-error-handling">error-handling</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-rest-utils">rest-utils</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-fiber-server-utils">fiber-server-utils</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-stomp-websocket">stomp-websocket</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-paas-mediation-client">paas-mediation-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-bg-state-monitor">bg-state-monitor</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-bg-kafka">bg-kafka</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-maas-core">maas-core</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-maas-client">maas-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-maas-segmentio">maas-segmentio</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-maas-bg-segmentio">maas-bg-segmentio</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-dbaas-base-client">dbaas-base-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-dbaas-postgres-client">dbaas-postgres-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-dbaas-mongo-client">dbaas-mongo-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-dbaas-cassandra-client">dbaas-cassandra-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-dbaas-opensearch-client">dbaas-opensearch-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-dbaas-arangodb-client">dbaas-arangodb-client</a> · <a href="https://github.com/Netcracker/qubership-core-lib-go-dbaas-clickhouse-client">dbaas-clickhouse-client</a></p>
        <p><b>Build &amp; tooling</b><br>
        <a href="https://github.com/Netcracker/qubership-core-infra">qubership-core-infra</a> · <a href="https://github.com/Netcracker/qubership-core-bootstrap">qubership-core-bootstrap</a> · <a href="https://github.com/Netcracker/qubership-core-base-images">qubership-core-base-images</a> · <a href="https://github.com/Netcracker/qubership-core-bulk-release">qubership-core-bulk-release</a> · <a href="https://github.com/Netcracker/qubership-core-test-apps">qubership-core-test-apps</a></p>
      </details>
    </td>
    <td valign="top" width="50%">
      <h3>📈 Observability</h3>
      <p>Monitoring, logging, tracing and profiling for cloud-native platforms — operators, exporters, plugins and OpenTelemetry tooling.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-monitoring-operator">qubership-monitoring-operator</a> — monitoring stack</li>
        <li><a href="https://github.com/Netcracker/qubership-logging-operator">qubership-logging-operator</a> — logging stack</li>
        <li><a href="https://github.com/Netcracker/qubership-jaeger">qubership-jaeger</a> — distributed tracing</li>
        <li><a href="https://github.com/Netcracker/qubership-open-telemetry-collector">qubership-open-telemetry-collector</a> — OTel Collector build</li>
        <li><a href="https://github.com/Netcracker/qubership-profiler-agent">qubership-profiler-agent</a> — Java profiler</li>
      </ul>
      <details>
        <summary><b>All 30 repositories</b></summary>
        <p><b>Monitoring</b><br>
        <a href="https://github.com/Netcracker/qubership-monitoring-operator">qubership-monitoring-operator</a> · <a href="https://github.com/Netcracker/qubership-prometheus-adapter-operator">qubership-prometheus-adapter-operator</a> · <a href="https://github.com/Netcracker/qubership-grafana-operator-converter">qubership-grafana-operator-converter</a> · <a href="https://github.com/Netcracker/qubership-grafana-plugins-init">qubership-grafana-plugins-init</a> · <a href="https://github.com/Netcracker/qubership-grafana-reporter">qubership-grafana-reporter</a> · <a href="https://github.com/Netcracker/qubership-graphite-remote-adapter">qubership-graphite-remote-adapter</a> · <a href="https://github.com/Netcracker/qubership-version-exporter">qubership-version-exporter</a> · <a href="https://github.com/Netcracker/qubership-network-latency-exporter">qubership-network-latency-exporter</a></p>
        <p><b>Logging</b><br>
        <a href="https://github.com/Netcracker/qubership-logging-operator">qubership-logging-operator</a> · <a href="https://github.com/Netcracker/qubership-fluentd">qubership-fluentd</a> · <a href="https://github.com/Netcracker/qubership-external-logging-installer">qubership-external-logging-installer</a> · <a href="https://github.com/Netcracker/qubership-graylog-auth-proxy">qubership-graylog-auth-proxy</a> · <a href="https://github.com/Netcracker/qubership-graylog-archiving-plugin">qubership-graylog-archiving-plugin</a> · <a href="https://github.com/Netcracker/qubership-graylog-obfuscation-plugin">qubership-graylog-obfuscation-plugin</a> · <a href="https://github.com/Netcracker/qubership-graylog-plugins-init">qubership-graylog-plugins-init</a> · <a href="https://github.com/Netcracker/qubership-logql-to-logsql-proxy">qubership-logql-to-logsql-proxy</a> · <a href="https://github.com/Netcracker/qubership-log-exporter">qubership-log-exporter</a> · <a href="https://github.com/Netcracker/qubership-log-generator">qubership-log-generator</a> · <a href="https://github.com/Netcracker/qubership-kube-events-reader">qubership-kube-events-reader</a> · <a href="https://github.com/Netcracker/qubership-kube-events-generator">qubership-kube-events-generator</a> · <a href="https://github.com/Netcracker/qubership-tcp-duplicator">qubership-tcp-duplicator</a></p>
        <p><b>Tracing &amp; profiling</b><br>
        <a href="https://github.com/Netcracker/qubership-jaeger">qubership-jaeger</a> · <a href="https://github.com/Netcracker/qubership-open-telemetry-collector">qubership-open-telemetry-collector</a> · <a href="https://github.com/Netcracker/qubership-diag-proxy">qubership-diag-proxy</a> · <a href="https://github.com/Netcracker/qubership-profiler-agent">qubership-profiler-agent</a> · <a href="https://github.com/Netcracker/qubership-profiler-backend">qubership-profiler-backend</a></p>
        <p><b>Tools &amp; examples</b><br>
        <a href="https://github.com/Netcracker/qubership-observability">qubership-observability</a> · <a href="https://github.com/Netcracker/qubership-env-checker">qubership-env-checker</a> · <a href="https://github.com/Netcracker/qubership-inventory-tool-cli">qubership-inventory-tool-cli</a> · <a href="https://github.com/Netcracker/robot-shop">robot-shop</a></p>
      </details>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <h3>⚓ Kubernetes Platform</h3>
      <p>Cluster lifecycle, disaster recovery, ingress and networking for Kubernetes.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/KubeMarine">KubeMarine</a> — cluster deployment &amp; maintenance</li>
        <li><a href="https://github.com/Netcracker/DRNavigator">DRNavigator</a> · <a href="https://github.com/Netcracker/qubership-disaster-recovery-daemon">disaster-recovery-daemon</a> — DR switchover</li>
        <li><a href="https://github.com/Netcracker/qubership-envoy-api-gateway">qubership-envoy-api-gateway</a> — Envoy Gateway chart</li>
        <li><a href="https://github.com/Netcracker/qubership-network-policy-operator">qubership-network-policy-operator</a> — Calico policies</li>
      </ul>
      <details>
        <summary><b>All 10 repositories</b></summary>
        <p><b>Cluster lifecycle</b><br>
        <a href="https://github.com/Netcracker/KubeMarine">KubeMarine</a> · <a href="https://github.com/Netcracker/qubership-cluster-management">qubership-cluster-management</a> · <a href="https://github.com/Netcracker/k8s-conformance">k8s-conformance</a> · <a href="https://github.com/Netcracker/qubership-docker-kubectl">qubership-docker-kubectl</a></p>
        <p><b>Disaster recovery &amp; backup</b><br>
        <a href="https://github.com/Netcracker/DRNavigator">DRNavigator</a> · <a href="https://github.com/Netcracker/qubership-disaster-recovery-daemon">qubership-disaster-recovery-daemon</a> · <a href="https://github.com/Netcracker/velero-patches">velero-patches</a></p>
        <p><b>Networking &amp; ingress</b><br>
        <a href="https://github.com/Netcracker/qubership-envoy-api-gateway">qubership-envoy-api-gateway</a> · <a href="https://github.com/Netcracker/qubership-network-policy-operator">qubership-network-policy-operator</a> · <a href="https://github.com/Netcracker/ingress-nginx">ingress-nginx</a></p>
      </details>
    </td>
    <td valign="top" width="50%">
      <h3>🗄 Data &amp; Messaging Services</h3>
      <p>Kubernetes operators with backup, monitoring and DBaaS adapters for databases, brokers and object storage.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/pgskipper-operator">pgskipper-operator</a> — PostgreSQL (Patroni)</li>
        <li><a href="https://github.com/Netcracker/qubership-kafka">qubership-kafka</a> · <a href="https://github.com/Netcracker/qubership-rabbitmq">qubership-rabbitmq</a> — messaging</li>
        <li><a href="https://github.com/Netcracker/qubership-opensearch">qubership-opensearch</a> · <a href="https://github.com/Netcracker/qubership-cassandra-operator">cassandra-operator</a> · <a href="https://github.com/Netcracker/qubership-mongodb-operator">mongodb-operator</a></li>
        <li><a href="https://github.com/Netcracker/qubership-consul">qubership-consul</a> · <a href="https://github.com/Netcracker/qubership-zookeeper">qubership-zookeeper</a> · <a href="https://github.com/Netcracker/qubership-redis">qubership-redis</a> · <a href="https://github.com/Netcracker/qubership-minio">qubership-minio</a></li>
      </ul>
      <details>
        <summary><b>All 61 repositories</b></summary>
        <p><b>PostgreSQL</b><br>
        <a href="https://github.com/Netcracker/pgskipper-operator">pgskipper-operator</a> · <a href="https://github.com/Netcracker/pgskipper-operator-core">pgskipper-operator-core</a> · <a href="https://github.com/Netcracker/pgskipper-patroni">pgskipper-patroni</a> · <a href="https://github.com/Netcracker/pgskipper-backup-daemon">pgskipper-backup-daemon</a> · <a href="https://github.com/Netcracker/pgskipper-pgbackrest-sidecar">pgskipper-pgbackrest-sidecar</a> · <a href="https://github.com/Netcracker/pgskipper-dbaas-adapter">pgskipper-dbaas-adapter</a> · <a href="https://github.com/Netcracker/pgskipper-monitoring-agent">pgskipper-monitoring-agent</a> · <a href="https://github.com/Netcracker/pgskipper-replication-controller">pgskipper-replication-controller</a> · <a href="https://github.com/Netcracker/pgskipper-upgrade">pgskipper-upgrade</a> · <a href="https://github.com/Netcracker/pg_hint_plan">pg_hint_plan</a> · <a href="https://github.com/Netcracker/postgres">postgres</a> · <a href="https://github.com/Netcracker/postgres-patches">postgres-patches</a></p>
        <p><b>Cassandra</b><br>
        <a href="https://github.com/Netcracker/qubership-cassandra-operator">qubership-cassandra-operator</a> · <a href="https://github.com/Netcracker/qubership-cassandra">qubership-cassandra</a> · <a href="https://github.com/Netcracker/qubership-cassandra-backup-daemon">qubership-cassandra-backup-daemon</a> · <a href="https://github.com/Netcracker/qubership-cassandra-medusa">qubership-cassandra-medusa</a> · <a href="https://github.com/Netcracker/qubership-cassandra-reaper">qubership-cassandra-reaper</a> · <a href="https://github.com/Netcracker/qubership-cassandra-tests">qubership-cassandra-tests</a> · <a href="https://github.com/Netcracker/qubership-cql-driver">qubership-cql-driver</a> · <a href="https://github.com/Netcracker/cassandra-exporter">cassandra-exporter</a> · <a href="https://github.com/Netcracker/cassandra">cassandra</a> · <a href="https://github.com/Netcracker/cassandra-patches">cassandra-patches</a></p>
        <p><b>MongoDB</b><br>
        <a href="https://github.com/Netcracker/qubership-mongodb-operator">qubership-mongodb-operator</a> · <a href="https://github.com/Netcracker/qubership-mongodb">qubership-mongodb</a> · <a href="https://github.com/Netcracker/qubership-mongodb-driver">qubership-mongodb-driver</a> · <a href="https://github.com/Netcracker/qubership-mongodb-prometheus-exporter">qubership-mongodb-prometheus-exporter</a></p>
        <p><b>OpenSearch</b><br>
        <a href="https://github.com/Netcracker/qubership-opensearch">qubership-opensearch</a> · <a href="https://github.com/Netcracker/qubership-docker-opensearch">qubership-docker-opensearch</a> · <a href="https://github.com/Netcracker/qubership-opensearch-curator">qubership-opensearch-curator</a> · <a href="https://github.com/Netcracker/qubership-opensearch-dbaas-adapter">qubership-opensearch-dbaas-adapter</a> · <a href="https://github.com/Netcracker/qubership-opensearch-monitoring">qubership-opensearch-monitoring</a> · <a href="https://github.com/Netcracker/opensearch-patches">opensearch-patches</a> · <a href="https://github.com/Netcracker/opensearch-cross-cluster-replication-patches">opensearch-cross-cluster-replication-patches</a></p>
        <p><b>Kafka &amp; RabbitMQ</b><br>
        <a href="https://github.com/Netcracker/qubership-kafka">qubership-kafka</a> · <a href="https://github.com/Netcracker/qubership-kafka-security">qubership-kafka-security</a> · <a href="https://github.com/Netcracker/qubership-akhq-build">qubership-akhq-build</a> · <a href="https://github.com/Netcracker/kafka">kafka</a> · <a href="https://github.com/Netcracker/kafka-patches">kafka-patches</a> · <a href="https://github.com/Netcracker/qubership-rabbitmq">qubership-rabbitmq</a> · <a href="https://github.com/Netcracker/rabbitmq-patches">rabbitmq-patches</a></p>
        <p><b>Consul &amp; ZooKeeper</b><br>
        <a href="https://github.com/Netcracker/qubership-consul">qubership-consul</a> · <a href="https://github.com/Netcracker/qubership-consul-backup-daemon">qubership-consul-backup-daemon</a> · <a href="https://github.com/Netcracker/qubership-consul-acl-configurator">qubership-consul-acl-configurator</a> · <a href="https://github.com/Netcracker/consul-patches">consul-patches</a> · <a href="https://github.com/Netcracker/qubership-zookeeper">qubership-zookeeper</a></p>
        <p><b>Other databases</b><br>
        <a href="https://github.com/Netcracker/qubership-redis">qubership-redis</a> · <a href="https://github.com/Netcracker/qubership-clickhouse-operator-helm">qubership-clickhouse-operator-helm</a> · <a href="https://github.com/Netcracker/arangodb">arangodb</a> · <a href="https://github.com/Netcracker/arangodb-patches">arangodb-patches</a></p>
        <p><b>Object storage</b><br>
        <a href="https://github.com/Netcracker/qubership-minio">qubership-minio</a> · <a href="https://github.com/Netcracker/qubership-minio-object-browser">qubership-minio-object-browser</a> · <a href="https://github.com/Netcracker/minio">minio</a> · <a href="https://github.com/Netcracker/minio-patches">minio-patches</a> · <a href="https://github.com/Netcracker/openmaxio-object-browser">openmaxio-object-browser</a></p>
        <p><b>Shared components</b><br>
        <a href="https://github.com/Netcracker/qubership-nosqldb-operator-core">qubership-nosqldb-operator-core</a> · <a href="https://github.com/Netcracker/qubership-backup-daemon">qubership-backup-daemon</a> · <a href="https://github.com/Netcracker/qubership-backup-daemon-go">qubership-backup-daemon-go</a> · <a href="https://github.com/Netcracker/qubership-deployment-status-provisioner">qubership-deployment-status-provisioner</a> · <a href="https://github.com/Netcracker/qubership-docker-integration-tests">qubership-docker-integration-tests</a> · <a href="https://github.com/Netcracker/qubership-query-exporter">qubership-query-exporter</a> · <a href="https://github.com/Netcracker/get-package-ids">get-package-ids</a></p>
      </details>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <h3>🌊 Data Processing &amp; Workflows</h3>
      <p>Dataflow, orchestration and analytics engines packaged for Kubernetes.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-nifi">qubership-nifi</a> · <a href="https://github.com/Netcracker/qubership-nifi-registry">nifi-registry</a> — Apache NiFi dataflows</li>
        <li><a href="https://github.com/Netcracker/qubership-airflow">qubership-airflow</a> — workflow orchestration</li>
        <li><a href="https://github.com/Netcracker/qubership-spark-on-k8s">qubership-spark-on-k8s</a> · <a href="https://github.com/Netcracker/qubership-trino">qubership-trino</a> — analytics</li>
        <li><a href="https://github.com/Netcracker/qubership-mistral">qubership-mistral</a> — workflow service</li>
      </ul>
      <details>
        <summary><b>All 9 repositories</b></summary>
        <p><b>Dataflow</b><br>
        <a href="https://github.com/Netcracker/qubership-nifi">qubership-nifi</a> · <a href="https://github.com/Netcracker/qubership-nifi-registry">qubership-nifi-registry</a></p>
        <p><b>Workflow orchestration</b><br>
        <a href="https://github.com/Netcracker/qubership-airflow">qubership-airflow</a> · <a href="https://github.com/Netcracker/qubership-mistral">qubership-mistral</a> · <a href="https://github.com/Netcracker/mistral-upstream">mistral-upstream</a></p>
        <p><b>Analytics</b><br>
        <a href="https://github.com/Netcracker/qubership-spark-on-k8s">qubership-spark-on-k8s</a> · <a href="https://github.com/Netcracker/qubership-trino">qubership-trino</a> · <a href="https://github.com/Netcracker/qubership-hive-metastore">qubership-hive-metastore</a> · <a href="https://github.com/Netcracker/qubership-hue">qubership-hue</a></p>
      </details>
    </td>
    <td valign="top" width="50%">
      <h3>🚀 DevOps &amp; Delivery</h3>
      <p>Reusable CI/CD building blocks and pipeline tooling used across the org.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-workflow-hub">qubership-workflow-hub</a> — reusable GitHub Actions</li>
        <li><a href="https://github.com/Netcracker/qubership-pipelines-declarative-executor">qubership-pipelines-declarative-executor</a> — declarative pipelines</li>
        <li><a href="https://github.com/Netcracker/qubership-git-system-follower">qubership-git-system-follower</a> — package manager for Git providers</li>
        <li><a href="https://github.com/Netcracker/qubership-build-info-go">qubership-build-info-go</a> — build-info generator</li>
      </ul>
      <details>
        <summary><b>All 20 repositories</b></summary>
        <p><b>CI/CD</b><br>
        <a href="https://github.com/Netcracker/qubership-workflow-hub">qubership-workflow-hub</a> · <a href="https://github.com/Netcracker/platform-ci-toolkit">platform-ci-toolkit</a> · <a href="https://github.com/Netcracker/qubership-test-pipelines">qubership-test-pipelines</a> · <a href="https://github.com/Netcracker/release-drafter">release-drafter</a> · <a href="https://github.com/Netcracker/chart-releaser-action">chart-releaser-action</a></p>
        <p><b>Pipelines</b><br>
        <a href="https://github.com/Netcracker/qubership-pipelines-declarative-executor">qubership-pipelines-declarative-executor</a> · <a href="https://github.com/Netcracker/qubership-pipelines-common-python-library">qubership-pipelines-common-python-library</a> · <a href="https://github.com/Netcracker/qubership-pipelines-cli-command-samples">qubership-pipelines-cli-command-samples</a> · <a href="https://github.com/Netcracker/qubership-pipelines-modules-ops">qubership-pipelines-modules-ops</a> · <a href="https://github.com/Netcracker/qubership-pde-operator">qubership-pde-operator</a></p>
        <p><b>Delivery tooling</b><br>
        <a href="https://github.com/Netcracker/qubership-git-system-follower">qubership-git-system-follower</a> · <a href="https://github.com/Netcracker/qubership-build-info-go">qubership-build-info-go</a> · <a href="https://github.com/Netcracker/qubership-app-manifest">qubership-app-manifest</a> · <a href="https://github.com/Netcracker/qubership-terraform-hub">qubership-terraform-hub</a> · <a href="https://github.com/Netcracker/qubership-colly">qubership-colly</a> · <a href="https://github.com/Netcracker/qubership-hub-test">qubership-hub-test</a></p>
        <p><b>Org tooling</b><br>
        <a href="https://github.com/Netcracker/qubership-repo-template">qubership-repo-template</a> · <a href="https://github.com/Netcracker/renovate-config">renovate-config</a> · <a href="https://github.com/Netcracker/qubership-landscape-config">qubership-landscape-config</a> · <a href="https://github.com/Netcracker/qubership-landscape-config-processor">qubership-landscape-config-processor</a></p>
      </details>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <h3>🧬 EnvGene</h3>
      <p>Environment generation and configuration management as code.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-envgene">qubership-envgene</a> — environment generator</li>
        <li><a href="https://github.com/Netcracker/qubership-envgene-base-modules">qubership-envgene-base-modules</a> — base modules</li>
        <li><a href="https://github.com/Netcracker/qubership-envgene-template">qubership-envgene-template</a> — starter template</li>
        <li><a href="https://github.com/Netcracker/qubership-cloud-passport-cli">qubership-cloud-passport-cli</a> — cloud passport CLI</li>
      </ul>
      <details>
        <summary><b>All 5 repositories</b></summary>
        <p><b>All</b><br>
        <a href="https://github.com/Netcracker/qubership-envgene">qubership-envgene</a> · <a href="https://github.com/Netcracker/qubership-envgene-base-modules">qubership-envgene-base-modules</a> · <a href="https://github.com/Netcracker/qubership-envgene-template">qubership-envgene-template</a> · <a href="https://github.com/Netcracker/qubership-envgene-instance">qubership-envgene-instance</a> · <a href="https://github.com/Netcracker/qubership-cloud-passport-cli">qubership-cloud-passport-cli</a></p>
      </details>
    </td>
    <td valign="top" width="50%">
      <h3>🧪 Testing Platform</h3>
      <p>Integration testing framework with system stubs, test data management and runners for popular test tools.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-testing-platform-itf-executor">itf-executor</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-itf-stubs">itf-stubs</a> — integrations testing framework</li>
        <li><a href="https://github.com/Netcracker/qubership-testing-platform-tdm">tdm</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-datasets">datasets</a> — test data</li>
        <li><a href="https://github.com/Netcracker/qubership-testing-platform-playwright-runner">playwright</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-bruno-runner">bruno</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-newman-runner">newman</a> runners</li>
      </ul>
      <details>
        <summary><b>All 32 repositories</b></summary>
        <p><b>Integrations Testing Framework</b> <sub><code>qubership-testing-platform-*</code></sub><br>
        <a href="https://github.com/Netcracker/qubership-testing-platform-itf-executor">itf-executor</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-itf-stubs">itf-stubs</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-itf-reporting">itf-reporting</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-itf-lite-backend">itf-lite-backend</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-itflite-script-engine">itflite-script-engine</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-itf-core-library">itf-core-library</a></p>
        <p><b>Test data &amp; environments</b> <sub><code>qubership-testing-platform-*</code></sub><br>
        <a href="https://github.com/Netcracker/qubership-testing-platform-tdm">tdm</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-tdm3">tdm3</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-datasets">datasets</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-environments">environments</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-ram">ram</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-mia">mia</a></p>
        <p><b>Runners</b> <sub><code>qubership-testing-platform-*</code></sub><br>
        <a href="https://github.com/Netcracker/qubership-testing-platform-playwright-runner">playwright-runner</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-bruno-runner">bruno-runner</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-newman-runner">newman-runner</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-python-runner">python-runner</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-common-scripts">common-scripts</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-helm-hook-helper">helm-hook-helper</a></p>
        <p><b>Libraries</b> <sub><code>qubership-testing-platform-*</code></sub><br>
        <a href="https://github.com/Netcracker/qubership-testing-platform-common-library">common-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-auth-library">auth-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-crypt-library">crypt-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-multitenancy-library">multitenancy-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-common-auditing-library">common-auditing-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-integration-library">integration-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-export-import-library">export-import-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-macros-core-library">macros-core-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-processcomparator-library">processcomparator-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-configuration-dataset-excel-library">configuration-dataset-excel-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-adapter-robot-library">adapter-robot-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-ss7-transport-library">ss7-transport-library</a> · <a href="https://github.com/Netcracker/qubership-testing-platform-diameter-transport-library">diameter-transport-library</a></p>
        <p><b>Results</b><br>
        <a href="https://github.com/Netcracker/qubership-testing-results">qubership-testing-results</a></p>
      </details>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <h3>🔐 Security</h3>
      <p>Authorization, identity, secrets and policy enforcement for Kubernetes workloads.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-authz-agent">qubership-authz-agent</a> — OPA-based authorization proxy</li>
        <li><a href="https://github.com/Netcracker/qubership-openbao">qubership-openbao</a> — secrets management</li>
        <li><a href="https://github.com/Netcracker/keycloak">keycloak</a> — identity &amp; access management</li>
        <li><a href="https://github.com/Netcracker/gatekeeper-library">gatekeeper-library</a> — OPA Gatekeeper policies</li>
      </ul>
      <details>
        <summary><b>All 8 repositories</b></summary>
        <p><b>Access &amp; identity</b><br>
        <a href="https://github.com/Netcracker/qubership-authz-agent">qubership-authz-agent</a> · <a href="https://github.com/Netcracker/keycloak">keycloak</a> · <a href="https://github.com/Netcracker/keycloak-patches">keycloak-patches</a></p>
        <p><b>Secrets</b><br>
        <a href="https://github.com/Netcracker/qubership-openbao">qubership-openbao</a> · <a href="https://github.com/Netcracker/qubership-credential-manager">qubership-credential-manager</a></p>
        <p><b>Policies &amp; scanning</b><br>
        <a href="https://github.com/Netcracker/gatekeeper-library">gatekeeper-library</a> · <a href="https://github.com/Netcracker/qubership-av-scan-service">qubership-av-scan-service</a> · <a href="https://github.com/Netcracker/qubership-3rd-party-security-report">qubership-3rd-party-security-report</a></p>
      </details>
    </td>
    <td valign="top" width="50%">
      <h3>🤖 AI Engineering</h3>
      <p>Tooling for teams working with AI coding agents.</p>
      <ul>
        <li><a href="https://github.com/Netcracker/qubership-ai-packages">qubership-ai-packages</a> — skills &amp; instructions for Claude Code, Codex, Cursor, Copilot</li>
        <li><a href="https://github.com/Netcracker/qubership-ai-agent-telemetry">qubership-ai-agent-telemetry</a> — OpenTelemetry for agent runs</li>
        <li><a href="https://github.com/Netcracker/qubership-virtual-secretary">qubership-virtual-secretary</a> — GenAI team assistant</li>
      </ul>
    </td>
  </tr>
</table>
