/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    if (head == NULL || head->next == NULL) return NULL;

    struct ListNode *fast=head, *slow=head;
 
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (fast == slow) break;        
    }

    if (fast == NULL || fast->next == NULL) return NULL;

    fast = head;

    while (fast!=slow) {
        fast = fast->next;
        slow = slow->next;
    }
 
 //printf("\n fast = %d", fast->val);
 //printf("\n slow = %d", slow->val); 
 return slow;
 /*
    bool no_circle = 0;
    int id_slow=0, id_fast=0;

    fast = fast->next;

    if (fast == NULL ||fast->next == NULL) return NULL;
    while(fast->next != NULL) {
        printf("\n 0. slow->val = %d   fast->val = %d", slow->val, fast->val);
        if (fast->next == head) return head;
        if (fast->next != NULL && fast->next == slow) {
            printf("\n 1. slow->val = %d   fast->val = %d", slow->val, fast->val);
            return slow;
        }
        fast = fast->next;
        no_circle = 1;
        if (fast->next == head) return head;
        if (fast->next != NULL && fast->next == slow) {
            printf("\n 2. slow->val = %d   fast->val = %d", slow->val, fast->val);
            return slow;
        }
        if (fast->next == head) return head;
        if (fast->next != NULL) {
            fast = fast->next;
            slow = slow->next;
            printf("\n 3. slow->val = %d   fast->val = %d", slow->val, fast->val);
        }
        if (fast->next == head) return head;

    }
printf("\n out slow->val = %d", slow->val);
printf("\n out no_circle = %d", no_circle);
    if (no_circle) return NULL;
    return slow;

*/
}