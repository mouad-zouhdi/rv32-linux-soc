// Module trivial de validation de la chaîne (phase 0)
module counter #(
  parameter int Width = 8
) (
  input  logic             clk_i,
  input  logic             rst_ni,
  input  logic             en_i,
  output logic [Width-1:0] count_o
);
  logic [Width-1:0] count_d, count_q;

  always_comb begin
    count_d = count_q;
    if (en_i) count_d = count_q + 1'b1;
  end

  always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) count_q <= '0;
    else         count_q <= count_d;
  end

  assign count_o = count_q;
endmodule
