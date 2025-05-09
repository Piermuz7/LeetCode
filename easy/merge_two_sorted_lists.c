/* 
You are given the heads of two sorted linked nodes node1 and node2.

Merge the two nodes into one sorted node.
The node should be made by splicing together the nodes of the first two nodes.

Return the head of the merged linked node.

Example 1:
Input: node1 = [1,2,4], node2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: node1 = [], node2 = []
Output: []

Example 3:
Input: node1 = [], node2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both nodes is in the range [0, 50].
-100 <= Node.val <= 100
Both node1 and node2 are sorted in non-decreasing order.
*/

#include<stdio.h>
#include<stdlib.h>


//Definition for singly-linked node.
struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *mergedLists = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *ptr = mergedLists;
    
    // Both empty lists
    if(list1 == NULL && list2 == NULL)
        return NULL;

    // One empty list
    if(list1 != NULL && list2 == NULL)
        return list1;
    if(list2 != NULL && list1 == NULL)
        return list2;

    while(list1 != NULL || list2 != NULL){
        if(list1 != NULL && list2 != NULL && (list1->val <= list2->val)){
            ptr->val = list1->val;
            list1 = list1->next;
        }
        else if((list2 != NULL)){
            ptr->val = list2->val;
            list2 = list2->next;
        }
        else if((list1 != NULL)){
            ptr->val = list1->val;
            list1 = list1->next;
        }
        if(list1 == NULL && list2 == NULL)
            ptr->next = NULL;
        else{
            ptr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            ptr = ptr->next;
        }
    }
    return mergedLists;
}

void printList(struct ListNode *node){
    int i = 0;
    while(node != NULL){
        printf("Node %d = %d\n", i, node->val);
        i++;
        node = node->next;
    }
}

int main(){

    struct ListNode *node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *node2 = (struct ListNode*)malloc(sizeof(struct ListNode));

    // node1
    node1->val = 1;
    node1->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    node1->next->val = 2;
    node1->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    node1->next->next->val = 4;
    node1->next->next->next = NULL;

    printf("List 1\n");
    printList(node1);

    // node2
    node2->val = 1;
    node2->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    node2->next->val = 3;
    node2->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    node2->next->next->val = 4;
    node2->next->next->next = NULL;

    printf("List 2\n");
    printList(node2);


    struct ListNode *mergednode = mergeTwoLists(node1, node2);

    printf("Merged Lists\n");
    printList(mergednode);

    return 0;
}