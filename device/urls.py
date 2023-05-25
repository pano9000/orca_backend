from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]



crm_acl_stats_acl_group_used_lag_egress=GaugeMetricFamily('crm_acl_stats_acl_group_used_lag_egress','crm_acl_stats_acl_group_used_lag_egress')
crm_acl_stats_acl_table_used_port_egress=GaugeMetricFamily('crm_acl_stats_acl_table_used_port_egress','crm_acl_stats_acl_table_used_port_egress')
crm_acl_stats_acl_group_available_rif_egress=GaugeMetricFamily('crm_acl_stats_acl_group_available_rif_egress','crm_acl_stats_acl_group_available_rif_egress')
crm_acl_stats_acl_table_available_switch_egress=GaugeMetricFamily('crm_acl_stats_acl_table_available_switch_egress','crm_acl_stats_acl_table_available_switch_egress')
crm_acl_stats_acl_table_available_vlan_egress=GaugeMetricFamily('crm_acl_stats_acl_table_available_vlan_egress','crm_acl_stats_acl_table_available_vlan_egress')
crm_acl_stats_acl_group_used_lag_ingress=GaugeMetricFamily('crm_acl_stats_acl_group_used_lag_ingress','crm_acl_stats_acl_group_used_lag_ingress')
crm_acl_stats_acl_table_used_port_ingress=GaugeMetricFamily('crm_acl_stats_acl_table_used_port_ingress','crm_acl_stats_acl_table_used_port_ingress')
crm_acl_stats_acl_group_available_rif_ingress=GaugeMetricFamily('crm_acl_stats_acl_group_available_rif_ingress','crm_acl_stats_acl_group_available_rif_ingress')
crm_acl_stats_acl_table_available_switch_ingress=GaugeMetricFamily('crm_acl_stats_acl_table_available_switch_ingress','crm_acl_stats_acl_table_available_switch_ingress')
crm_acl_stats_acl_table_available_vlan_ingress=GaugeMetricFamily('crm_acl_stats_acl_table_available_vlan_ingress','crm_acl_stats_acl_table_available_vlan_ingress')
crm_stats_dnat_entry_used=GaugeMetricFamily('crm_stats_dnat_entry_used','crm_stats_dnat_entry_used')
crm_stats_fdb_entry_used=GaugeMetricFamily('crm_stats_fdb_entry_used','crm_stats_fdb_entry_used')
crm_stats_ipmc_entry_used=GaugeMetricFamily('crm_stats_ipmc_entry_used','crm_stats_ipmc_entry_used')
crm_stats_ipv4_neighbor_used=GaugeMetricFamily('crm_stats_ipv4_neighbor_used','crm_stats_ipv4_neighbor_used')
crm_stats_ipv4_nexthop_used=GaugeMetricFamily('crm_stats_ipv4_nexthop_used','crm_stats_ipv4_nexthop_used')
crm_stats_ipv4_route_used=GaugeMetricFamily('crm_stats_ipv4_route_used','crm_stats_ipv4_route_used')
crm_stats_ipv6_neighbor_used=GaugeMetricFamily('crm_stats_ipv6_neighbor_used','crm_stats_ipv6_neighbor_used')
crm_stats_ipv6_nexthop_used=GaugeMetricFamily('crm_stats_ipv6_nexthop_used','crm_stats_ipv6_nexthop_used')
crm_stats_ipv6_route_used=GaugeMetricFamily('crm_stats_ipv6_route_used','crm_stats_ipv6_route_used')
crm_stats_nexthop_group_member_used=GaugeMetricFamily('crm_stats_nexthop_group_member_used','crm_stats_nexthop_group_member_used')
crm_stats_nexthop_group_used=GaugeMetricFamily('crm_stats_nexthop_group_used','crm_stats_nexthop_group_used')
crm_stats_snat_entry_used=GaugeMetricFamily('crm_stats_snat_entry_used','crm_stats_snat_entry_used')
crm_stats_dnat_entry_available=GaugeMetricFamily('crm_stats_dnat_entry_available','crm_stats_dnat_entry_available')
crm_stats_fdb_entry_available=GaugeMetricFamily('crm_stats_fdb_entry_available','crm_stats_fdb_entry_available')
crm_stats_ipmc_entry_available=GaugeMetricFamily('crm_stats_ipmc_entry_available','crm_stats_ipmc_entry_available')
crm_stats_ipv4_neighbor_available=GaugeMetricFamily('crm_stats_ipv4_neighbor_available','crm_stats_ipv4_neighbor_available')
crm_stats_ipv4_nexthop_available=GaugeMetricFamily('crm_stats_ipv4_nexthop_available','crm_stats_ipv4_nexthop_available')
crm_stats_ipv4_route_available=GaugeMetricFamily('crm_stats_ipv4_route_available','crm_stats_ipv4_route_available')
crm_stats_ipv6_neighbor_available=GaugeMetricFamily('crm_stats_ipv6_neighbor_available','crm_stats_ipv6_neighbor_available')
crm_stats_ipv6_nexthop_available=GaugeMetricFamily('crm_stats_ipv6_nexthop_available','crm_stats_ipv6_nexthop_available')
crm_stats_ipv6_route_available=GaugeMetricFamily('crm_stats_ipv6_route_available','crm_stats_ipv6_route_available')
crm_stats_nexthop_group_available=GaugeMetricFamily('crm_stats_nexthop_group_available','crm_stats_nexthop_group_available')
crm_stats_nexthop_group_member_available=GaugeMetricFamily('crm_stats_nexthop_group_member_available','crm_stats_nexthop_group_member_available')
crm_stats_snat_entry_available=GaugeMetricFamily('crm_stats_snat_entry_available','crm_stats_snat_entry_available')
