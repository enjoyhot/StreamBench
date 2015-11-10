package fi.aalto.dmg.frame;

import backtype.storm.topology.TopologyBuilder;
import backtype.storm.tuple.Fields;
import fi.aalto.dmg.frame.bolts.PairReduceBolt;
import fi.aalto.dmg.frame.functions.ReduceFunction;

/**
 * Created by yangjun.wang on 01/11/15.
 */
public class StormGroupedWorkloadOperator<K,V> implements GroupedWorkloadOperator<K,V>  {

    protected TopologyBuilder topologyBuilder;
    protected String preComponentId;

    public StormGroupedWorkloadOperator(TopologyBuilder builder, String previousComponent){
        this.topologyBuilder = builder;
        this.preComponentId = previousComponent;
    }

    @Override
    public PairWorkloadOperator<K, V> reduce(ReduceFunction<V> fun, String componentId) {

        topologyBuilder.setBolt(componentId, new PairReduceBolt<K,V>(fun)).fieldsGrouping(preComponentId, new Fields("key"));
        return new StormPairWordloadOperator<>(topologyBuilder, componentId);
    }
}