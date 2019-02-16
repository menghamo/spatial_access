#pragma once

#include <thread>
#include <mutex>
#include <vector>

#include "Graph.h"
#include "userDataContainer.h"
#include "dataFrame.h"

/* jobQueue: a thread-safe queue for dispensing integer jobs*/
class jobQueue {
private:
    std::vector <unsigned long int> data;
    mutable std::mutex lock;
public:
    jobQueue(unsigned long int size);
    void insert(unsigned long int item);
    unsigned long int pop(bool &endNow);
    bool empty() const;
};


template<class row_label_type, class col_label_type> class graphWorkerArgs;

/* A pool of worker threads to execute a job (f_in), which takes arguments (wa)*/
template<class row_label_type, class col_label_type>
class workerQueue {
private:
    std::vector<std::thread> threads;
public:
    workerQueue(unsigned int numThreads, void (*f_in)(graphWorkerArgs<row_label_type, col_label_type>*), graphWorkerArgs<row_label_type, col_label_type> *wa);
    void startGraphWorker();
};


template<class row_label_type, class col_label_type>
class graphWorkerArgs {
public:
    Graph &graph;
    dataFrame<row_label_type, col_label_type> &df;
    jobQueue jq;
    userDataContainer userSourceData;
    userDataContainer userDestData;
    unsigned long int numNodes;
    graphWorkerArgs(Graph &graph, userDataContainer &userSourceData,
                       userDataContainer &userDestData, 
                       int numNodes, dataFrame<row_label_type, col_label_type> &df)
    : graph(graph), df(df), jq(numNodes), userSourceData(userSourceData), userDestData(userDestData),
     numNodes(numNodes) {}
    void initialize();
};