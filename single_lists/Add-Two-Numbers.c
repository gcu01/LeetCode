/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int remainder = 0;
    struct ListNode *sum = (struct ListNode *) (malloc (sizeof (struct ListNode)));
    struct ListNode *head_sum = sum;
    sum->val = (l1->val + l2->val)%10;
    remainder = (l1->val + l2->val)/10;
    l1 = l1->next;
    l2 = l2->next;
printf("\n first step: sum->val = %d   remainder = %d", sum->val, remainder);
    while ((l1 != NULL || l2 != NULL) || remainder) {
        if (!l1 && l2) {
            sum->next = (struct ListNode *) (malloc (sizeof (struct ListNode)));
            sum = sum->next;
            sum->val = (l2->val + remainder)%10;
            remainder = (l2->val + remainder)/10;
            l2 = l2->next;
        } else if (l1 && !l2) {
            sum->next = (struct ListNode *) (malloc (sizeof (struct ListNode)));
            sum = sum->next;
            sum->val = (l1->val + remainder)%10;
            remainder = (l1->val + remainder)/10;
            l1 = l1->next;
        } else if (l1 && l2){
            sum->next = (struct ListNode *) (malloc (sizeof (struct ListNode)));
            sum = sum->next;
            sum->val = (l1->val + l2->val + remainder)%10;            
            remainder = (l1->val + l2->val + remainder)/10;
            l1 = l1->next;
            l2 = l2->next;
            printf("\n sum->val = %d   remainder = %d", sum->val, remainder);
        } else if ( remainder) {
            printf("\n remainder = %d", remainder);
            sum->next = (struct ListNode *) (malloc (sizeof (struct ListNode)));
            sum = sum->next;
            sum->val = remainder;
            remainder = 0;
        }
    }
    sum->next = NULL;
    return head_sum;
}