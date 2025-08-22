/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    
    if(head == NULL) return NULL;

    struct ListNode *newL = NULL, *headNewL = NULL;

    while (head != NULL) {
        if (head->val != val) {
            newL = (struct ListNode*) malloc(sizeof(struct ListNode));
            newL = head;
            newL->val = head->val;
            headNewL = newL;
            head = head->next;
            //printf("\n inside newL->val = %d \n", newL->val);
            break;
        }
        head = head->next;
    }
//if (head) printf("\n head->val = %d\n", head->val);
    while (head != NULL) {
        if (head->val != val) {
            newL->next = (struct ListNode*) malloc(sizeof(struct ListNode));
            newL = newL->next;
            newL->val = head->val;     
            //printf("\n inside 2nd while: newL->val = %d \n", newL->val);                  
        }
        //printf("\n newL->val = %d", newL->val);
        head = head->next;
        //if (head) printf("\n inside 2nd while: head->val = %d \n", head->val);
    }
    if (newL) newL->next = NULL;
    //newL = headNewL;
    //while(newL) {printf("\n out newL->val = %d", newL->val); newL = newL->next;}

    return headNewL;
}