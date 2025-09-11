/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if (!head) return head;
    if (head->next == NULL && n==1) return NULL;
    int init_n = n;

    struct ListNode *jump = head, *init = head;
    //printf("\n jump->val = %d", jump->val);
    while (head->next) {
        if (n>0) {
            head = head->next;
            n--;
        } else {
            head = head->next;  
            jump = jump->next;
        }
        //printf("\n jump = %p", jump);
    }

    //printf("\n jump = %p, init = %p, n = %d", jump, init, n);
   if (init == jump && init_n == 1 && n!=0) {
    jump->next = NULL;
   }  else if (init == jump && n!=0) {
    init = init->next;
   }
    else {
    jump->next = (jump->next)->next;
    }
    //printf("\n jump->val = %d init->val = %d", jump->val, init->val);
    return init;
}