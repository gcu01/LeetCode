/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    if (!head) return NULL;
    if (head->next == NULL) return head;
    if ((head->next)->next == NULL) return head->next;

    struct ListNode *slow = head, *fast  = head;

    while (fast != NULL && fast->next != NULL ) {
        //printf(" \n slow->val = %d fast->val = %d", slow->val, fast->val);
        slow = slow->next;//printf(" \n slow = %p slow->val = %d", slow, (slow->val));
        fast = (fast->next)->next;
        //printf(" \n fast = %p fast-val = %d", fast, (fast->val));
        //if ((fast->next)->next == NULL) return slow->next;

    }
    
    //printf(" \n odd = %d slow->val = %d", odd, slow->val);

    /* if (fast->next == NULL) {
        return slow;
    } 
    if ((fast->next)->next == NULL){
        return slow->next;
    }*/
    return slow;
}