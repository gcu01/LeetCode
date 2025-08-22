/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
*/

//passing by both lists, count the no. elements, see if the last one has the same pointer
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    int elemA = 0, elemB=0, pos = 0;
    void *lastA, *lastB;
    struct ListNode *nodeA = headA, *nodeB = headB;

    if (nodeA == NULL || nodeB == NULL) {
        return NULL;
    }
    if (nodeA == nodeB) {
        return nodeB;
    }

    while(nodeA) {
        elemA++;
        if (nodeA->next == NULL) {
            lastA = nodeA;
        }
        //printf("\n nodeA = %p", nodeA);
        nodeA = nodeA->next;
    }
//printf("\n ");
    while(nodeB) {
        elemB++;
        if (nodeB->next == NULL) {
            lastB = nodeB;
        }
        //printf("\n nodeB = %p", nodeB);
        nodeB = nodeB->next;
    }
//printf("\n ");
    //printf("\n elemA = %d, elemB = %d", elemA, elemB);

    if (nodeA != nodeB) {
        return NULL;
    }

    nodeA = headA;
    nodeB = headB;
 //printf("\n ");   
    while (nodeA && nodeB) {
        if (elemA > elemB) {
            for (int i = 0; i < (elemA-elemB); i++) {
                nodeA = nodeA->next;                
            }
        } else if (elemA < elemB) { 
            for (int i = 0; i < (elemB-elemA); i++) {
                nodeB = nodeB->next;
            }
        }
        elemA = elemB;
        //printf("\n nodeA = %p, nodeB = %p", nodeA, nodeB);
        if (nodeA == nodeB) {
            return nodeA;
        }
        nodeA = nodeA->next;
        nodeB = nodeB->next;
    }

    return NULL;
}


// it takes much memory to save all pointers in a vector of maximum size (30000 elements)
/*
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if (headA == NULL || headB == NULL) {
        return NULL;
    }
    if (headA == headB) {
        return headB;
    }
    
    struct ListNode *lstA[30000];
    int pos = 0;

    while(headA != NULL) {
        lstA[pos] = headA;
        pos++;
        headA = headA->next;
    }

    while(headB != NULL){
    //printf("\n headB = %p", headB);
        for (int i=0; i<=pos; i++) {
            //printf("\n lst[%d] = %p", i, lstA[i]);
            if (lstA[i] == headB) {
                return headB;
            }
        }        
        headB = headB->next;
    }

    return NULL;
}
*/