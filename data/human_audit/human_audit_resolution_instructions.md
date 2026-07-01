# Human Audit Disagreement Resolution Instructions

说明：本文档记录内部 disagreement resolution 流程。公开 artifact 不包含完整上下文、
hidden key、原始事件文本、完整代码/trace 或完整 rationale；公开版本只保留可复核
统计所需的 reduced labels、risk flags、aggregate metrics 和 2 条简短示意说明。

当前两位标注者已经完成独立标注。请先不要修改原始 A/B 标注文件。

## 当前状态

- 总案例数：80
- 两位标注者一致：55
- 两位标注者不一致：25
- 三分类 Cohen's kappa：0.270

这个 κ 值说明当前结果还不能直接作为最终人工金标准。需要对 25 条分歧案例进行讨论，形成最终 consensus label。

## 需要填写的文件

填写：

- `human_audit_disagreements_for_resolution_with_context.csv`

不要修改：

- `human_audit_annotations_annotator_a.csv`
- `human_audit_annotations_annotator_b.csv`
- 内部 hidden key 文件

## 填写列

请只填写以下列：

- `final_consensus_label`
- `consensus_rationale`
- `adjudicator_initials`
- `resolved`

`final_consensus_label` 只能使用：

- `code_defect`
- `faulty_test`
- `unclear`

`resolved` 填：

- `yes`：已经讨论并形成共识
- `no`：仍未解决

## 处理原则

1. 先看 problem statement 和 sample I/O。
2. 再看 generated test 的输入和 expected output 是否被规格支持。
3. 再看 candidate code 和 observed failure。
4. 如果 generated test 自己引入了规格外假设，标 `faulty_test`。
5. 如果 generated test 合理而代码没有满足规格，标 `code_defect`。
6. 如果规格本身不清楚、证据不足、代码和测试都可疑，标 `unclear`。

## 论文使用口径

最终论文中可以报告：

- 两位标注者的 independent agreement 和 Cohen's kappa。
- 分歧讨论后的 consensus label 上，Arbiter 与人工共识的一致率、Macro-F1、per-class F1。

不要把 preliminary Arbiter-human 指标当最终结果，因为目前它只基于 55 条双方一致样本。
