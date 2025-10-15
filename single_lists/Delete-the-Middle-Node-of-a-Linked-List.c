/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    if (head == NULL || head->next == NULL) return NULL;

    struct ListNode *slow=head, *fast=head, *prev=NULL;

    while(fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    } 
    prev->next = slow->next;
    //printf("\n slow=%d", slow->val);

    return head;
}